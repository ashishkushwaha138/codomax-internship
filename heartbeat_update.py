import json
import time
import subprocess
import os
from datetime import datetime, timezone

workspace = '/home/ubuntu/.openclaw/workspace'
state_path = os.path.join(workspace, 'heartbeat-state.json')
heartbeat_path = os.path.join(workspace, 'HEARTBEAT.md')

# Load state
with open(state_path, 'r') as f:
    state = json.load(f)

now = int(time.time())
state['lastChecks']['heartbeat'] = now

# Check if we need to update weather (every 30 minutes)
last_weather = state['lastChecks'].get('weather', 0)
if now - last_weather > 1800:  # 30 minutes
    try:
        # Use curl to get weather for Ashburn
        result = subprocess.run(['curl', '-s', 'wttr.in/Ashburn?format=3'], 
                                capture_output=True, text=True, timeout=10)
        weather_info = result.stdout.strip()
        if not weather_info:
            weather_info = "weather (error)"
    except Exception as e:
        weather_info = f"weather (error: {e})"
    # Update weather timestamp
    state['lastChecks']['weather'] = now
else:
    weather_info = "weather (skipped, recent)"

# Disk usage
try:
    disk_result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True, timeout=5)
    lines = disk_result.stdout.strip().split('\n')
    if len(lines) >= 2:
        disk_usage = lines[1].split()[4]  # Use percentage
    else:
        disk_usage = "unknown"
except Exception:
    disk_usage = "unknown"

# Memory usage
try:
    mem_result = subprocess.run(['free', '-h'], capture_output=True, text=True, timeout=5)
    lines = mem_result.stdout.strip().split('\n')
    if len(lines) >= 2:
        parts = lines[1].split()
        total = parts[1]
        used = parts[2]
        # Convert to GiB if they are in MiB or GiB
        def to_gib(x):
            if x.endswith('GiB'):
                return float(x[:-3])
            elif x.endswith('MiB'):
                return float(x[:-3]) / 1024
            elif x.endswith('KiB'):
                return float(x[:-3]) / 1024 / 1024
            else:  # assume bytes
                return float(x) / 1024 / 1024 / 1024
        used_gib = to_gib(used)
        total_gib = to_gib(total)
        mem_info = f"{used_gib:.1f}Gi/{total_gib:.1f}Gi"
    else:
        mem_info = "unknown"
except Exception:
    mem_info = "unknown"

# Git status
try:
    git_result = subprocess.run(['git', 'status', '--porcelain'], 
                                cwd=workspace, capture_output=True, text=True, timeout=5)
    git_status = git_result.stdout.strip()
    if git_status == '':
        git_msg = "git: clean"
    else:
        changes = len(git_status.split('\n'))
        git_msg = f"git: {changes} changes"
except Exception:
    git_msg = "git: unknown"

# Current time in UTC
current_iso = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

# Append to HEARTBEAT.md
with open(heartbeat_path, 'a') as f:
    f.write(f"[{current_iso}] Heartbeat poll processed. Weather: {weather_info}, Disk: {disk_usage}, Memory: {mem_info}, {git_msg}\n")

# Save state
with open(state_path, 'w') as f:
    json.dump(state, f, indent=2)

print("Heartbeat updated")

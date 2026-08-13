import json, os, subprocess, time
file_path = 'memory/heartbeat-state.json'
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    data = {'lastChecks': {}}
# Get current timestamp
timestamp = str(int(time.time()))
# Check if git is dirty
try:
    git_status = subprocess.check_output(['git', 'status', '--porcelain'], stderr=subprocess.STDOUT, universal_newlines=True)
    git_dirty = bool(git_status.strip())
except Exception as e:
    git_dirty = False
    print(f"Error checking git status: {e}")
# Update state
data['lastChecks']['heartbeat'] = timestamp
data['lastChecks']['gitDirty'] = git_dirty
with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)
# Append to HEARTBEAT.md
heartbeat_md = 'HEARTBEAT.md'
entry = f'- {timestamp} UTC: Heartbeat check. Git status: {"dirty" if git_dirty else "clean"}.\\n'
if os.path.exists(heartbeat_md):
    with open(heartbeat_md, 'r') as f:
        content = f.read()
else:
    content = '## Heartbeat Log\\n'
new_content = content + entry
with open(heartbeat_md, 'w') as f:
    f.write(new_content)
# Print message for logging
print(f'Heartbeat checked at {timestamp}. Git status: {"dirty" if git_dirty else "clean"}.')
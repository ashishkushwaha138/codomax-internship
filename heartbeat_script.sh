#!/bin/bash
cd /home/ubuntu/.openclaw/workspace
current_time=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
current_timestamp=$(date -u +%s)
weather=$(curl --max-time 5 -s "wttr.in/Ashburn?format=%C+%t" 2>/dev/null || echo "unavailable")
disk_usage=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')
memory_total_kb=$(awk '/MemTotal/ {print $2}' /proc/meminfo)
memory_available_kb=$(awk '/MemAvailable/ {print $2}' /proc/meminfo)
memory_used_kb=$((memory_total_kb - memory_available_kb))
memory_usage=$(awk -v total=$memory_total_kb -v used=$memory_used_kb 'BEGIN {printf "%.1fGi/%.1fGi", used/1024/1024, total/1024/1024}')
git_status=$(git status --porcelain | wc -l)
echo "{\"lastChecks\": {\"heartbeat\": $current_timestamp, \"gitDirty\": $( [ $git_status -eq 0 ] && echo false || echo true )}}" > memory/heartbeat-state.json
echo -e "\n## Heartbeat Update - $current_time\n\n**Weather:** $weather\n**System:** Disk usage: $disk_usage%, Memory: $memory_usage\n**Git:** $( [ $git_status -eq 0 ] && echo "clean" || echo "dirty" )\n**Notes:** Weather, disk, memory, and git checked at $current_time." >> HEARTBEAT.md
#!/bin/bash
set -e

cd /home/ubuntu/.openclaw/workspace

state=$(cat heartbeat-state.json)
heartbeat=$(echo "$state" | jq .lastChecks.heartbeat)
email=$(echo "$state" | jq .lastChecks.email)
calendar=$(echo "$state" | jq .lastChecks.calendar)
weather=$(echo "$state" | jq .lastChecks.weather)
social=$(echo "$state" | jq .lastChecks.social)
gitDirty=$(echo "$state" | jq .lastChecks.gitDirty)

current_time=$(date +%s)

new_state=$(echo "$state" | jq --argjson ct "$current_time" '.lastChecks.heartbeat = ($ct | tonumber)')

checks_done=()

# Email check - skip because no credentials
if [ $((current_time - email)) -gt 14400 ]; then
    # We would check email, but we don't have credentials.
    checks_done+=("email (skipped, no credentials)")
else
    checks_done+=("email (skipped, recent)")
fi

# Calendar check - skip because no credentials
if [ $((current_time - calendar)) -gt 14400 ]; then
    checks_done+=("calendar (skipped, no credentials)")
else
    checks_done+=("calendar (skipped, recent)")
fi

# Weather check
if [ $((current_time - weather)) -gt 21600 ]; then
    weather_result=$(curl -s wttr.in?format=3 2>/dev/null || echo "Weather check failed")
    checks_done+=("weather: $weather_result")
    new_state=$(echo "$new_state" | jq --argjson ct "$current_time" '.lastChecks.weather = ($ct | tonumber)')
else
    checks_done+=("weather (skipped, recent)")
fi

# Social check - skip because no credentials
checks_done+=("social (skipped, no credentials)")

# Git dirty check
git_status=$(git status --porcelain)
if [ -n "$git_status" ]; then
    new_gitDirty=true
    checks_done+=("git: dirty")
else
    new_gitDirty=false
    checks_done+=("git: clean")
fi
new_state=$(echo "$new_state" | jq --argjson gd "$new_gitDirty" '.lastChecks.gitDirty = $gd')

# Write new state
echo "$new_state" > heartbeat-state.json

# Append to HEARTBEAT.md
echo "- $(date -u +"%Y-%m-%d %H:%M:%S UTC") Heartbeat check: ${checks_done[*]}" >> HEARTBEAT.md

# Output the summary for the user
echo "Heartbeat check completed: ${checks_done[*]}"
#!/bin/bash
set -e

WORKSPACE="/home/ubuntu/.openclaw/workspace"
STATE_FILE="$WORKSPACE/memory/heartbeat-state.json"

# Initialize state file if not exists
if [ ! -f "$STATE_FILE" ]; then
    echo '{"lastChecks":{}}' > "$STATE_FILE"
fi

# Read state
STATE=$(cat "$STATE_FILE")
# Use python to get the last check times, default to 0 if not set or not a number
WEATHER_LAST=$(echo "$STATE" | python3 -c "import sys, json; data=json.load(sys.stdin); last=data.get('lastChecks',{}); print(int(last.get('weather',0)))" 2>/dev/null || echo 0)
MEMORY_LAST=$(echo "$STATE" | python3 -c "import sys, json; data=json.load(sys.stdin); last=data.get('lastChecks',{}); print(int(last.get('memory',0)))" 2>/dev/null || echo 0)
GIT_LAST=$(echo "$STATE" | python3 -c "import sys, json; data=json.load(sys.stdin); last=data.get('lastChecks',{}); print(int(last.get('git',0)))" 2>/dev/null || echo 0)

NOW=$(date +%s)
WEATHER_AGE=$((NOW - WEATHER_LAST))
MEMORY_AGE=$((NOW - MEMORY_LAST))
GIT_AGE=$((NOW - GIT_LAST))

# Determine the oldest check
if [ "$WEATHER_AGE" -ge "$MEMORY_AGE" ] && [ "$WEATHER_AGE" -ge "$GIT_AGE" ]; then
    CHECK="weather"
elif [ "$MEMORY_AGE" -ge "$WEATHER_AGE" ] && [ "$MEMORY_AGE" -ge "$GIT_AGE" ]; then
    CHECK="memory"
else
    CHECK="git"
fi

INTERESTING=""

case "$CHECK" in
    weather)
        # Fetch weather from wttr.in (using IP-based location)
        # We'll get a one-line report: wttr.in/?format=3
        WEATHER_REPORT=$(curl -s "wttr.in/?format=3" 2>/dev/null || echo "Unable to fetch weather")
        # Example: "London: +22.0°C ☀️"
        # We'll check if the temperature is extreme? Let's define extreme as below 0°C or above 35°C.
        # We'll extract the temperature.
        # The format is: "Location: +XX.X°C ..."
        # We'll extract the number after the colon and before the degree symbol.
        # We'll do a simple extraction: look for a pattern of + or - followed by numbers and a dot maybe.
        # We'll use grep and sed.
        TEMPERATURE=$(echo "$WEATHER_REPORT" | grep -oE '[+-]?[0-9]+\\.?[0-9]*°C' | sed 's/°C//')
        if [ -n "$TEMPERATURE" ]; then
            # Check if it's a number
            if [[ "$TEMPERATURE" =~ ^[+-]?[0-9]+\\.?[0-9]*$ ]]; then
                if (( $(echo "$TEMPERATURE < 0" | bc -l) )) || (( $(echo "$TEMPERATURE > 35" | bc -l) )); then
                    INTERESTING="Weather alert: $WEATHER_REPORT"
                fi
            fi
        else
            # If we couldn't extract temperature, we might still note if the report indicates something extreme?
            # For now, we don't.
            :
        fi
        ;;
    memory)
        # Check for memory files that are not today's and see if they have content worth folding.
        MEMORY_DIR="$WORKSPACE/memory"
        TODAY=$(date +%Y-%m-%d)
        # Find files in memory directory that are not today and are not empty
        # We'll look for files that are older than today (by name) and have content.
        # We'll skip today's file.
        OLD_MEMORIES=$(find "$MEMORY_DIR" -type f -name "*.md" ! -name "$TODAY.md" -size +0c 2>/dev/null || true)
        if [ -n "$OLD_MEMORIES" ]; then
            # We'll check each file for content that might be worth folding.
            # For simplicity, we'll just note that there are old memory files and suggest folding.
            INTERESTING="Found old memory files: $(echo "$OLD_MEMORIES" | wc -l) files not folded into MEMORY.md"
        else
            INTERESTING="No old memory files to fold."
        fi
        ;;
    git)
        # Check if the workspace is a git repo and if there are uncommitted changes.
        if [ -d "$WORKSPACE/.git" ]; then
            # We are in a git repo
            CHANGES=$(cd "$WORKSPACE" && git status --porcelain 2>/dev/null)
            if [ -n "$CHANGES" ]; then
                INTERESTING="Workspace has uncommitted changes:\\n$CHANGES"
            else
                INTERESTING="Workspace is clean."
            fi
        else
            INTERESTING="Workspace is not a git repo."
        fi
        ;;
esac

# Update the state for the check we just did
# We'll use python to update the JSON
python3 -c "
import sys, json
with open('$STATE_FILE', 'r') as f:
    data = json.load(f)
lastChecks = data.get('lastChecks', {})
lastChecks['$CHECK'] = $NOW
data['lastChecks'] = lastChecks
with open('$STATE_FILE', 'w') as f:
    json.dump(data, f, indent=2)
        "

# Output the interesting message if we have one
if [ -n "$INTERESTING" ]; then
    echo "$INTERESTING"
fi

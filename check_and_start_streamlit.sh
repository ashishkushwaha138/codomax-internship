#!/bin/bash
# Check if the Streamlit app is running on port 8501
if ! ss -tlnp | grep -q ':8501'; then
    echo "Streamlit app not running. Starting..."
    /home/ubuntu/.openclaw/workspace/start_streamlit.sh
else
    echo "Streamlit app is already running."
fi
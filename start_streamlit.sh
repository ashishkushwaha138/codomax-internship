#!/bin/bash
cd /home/ubuntu/.openclaw/workspace/CODSOFT_TASKSNO
source venv/bin/activate
nohup streamlit run streamlit_app.py --server.port=8501 --server.address=0.0.0.0 > streamlit.log 2>&1 &
echo $! > streamlit.pid
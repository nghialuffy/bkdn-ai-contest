#!/bin/bash
export TERM=xterm
Xvfb :20 -screen 0 1366x768x16 &
export DISPLAY=:20
cd /home/tool
echo "RUN TOOL"
python3 app.py
exec $@

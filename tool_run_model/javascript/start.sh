#!/bin/bash
export TERM=xterm
Xvfb :20 -screen 0 1366x768x16 &
export DISPLAY=:20
cd /app
echo "RUN TOOL"
while true;
do
    sleep 1
    python3 main.py
done
exec $@

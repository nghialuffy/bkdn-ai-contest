#!/bin/bash
export TERM=xterm
Xvfb :20 -screen 0 1366x768x16 &
export DISPLAY=:20
cd /home
echo "RUN TOOL"
while true;
do
    sleep 1
    python3 main.py
done &

while true;
do
    sleep 2
    python3 main.py
done &

while true;
do
    sleep 3
    python3 main.py
done &

while true;
do
    sleep 4
    python3 main.py
done &

while true;
do
    sleep 5
    python3 main.py
done
exec $@

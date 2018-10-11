#!/bin/bash
python3 ./server.py &
echo delay 3s
sleep 3
python3 ./client.py


#!/bin/bash
# Launch the Dragon Assistant

cd "$(dirname "$0")"
source env/bin/activate
python3 main.py

#MAKE IT EXECUTABLE
#chmod +x start_dragon.sh

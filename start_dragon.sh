#!/bin/bash
# Launch the Dragon Assistant

cd "$(dirname "$0")"
source env/bin/activate
python3 main.py

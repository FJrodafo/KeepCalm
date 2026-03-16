#!/bin/bash

# This script runs the Python command to generate a "Keep Calm" image.

venv/bin/python3 keep-calm.py \
    --width 400 \
    --text "keeeep" "caaaalm" "&" "continue" "coding" \
    --bg-colour "coral" \
    --text-colour "black" \
    --output ./output/continue_coding.png

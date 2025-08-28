#!/bin/bash
# Script to run the GUI with virtual display for testing

echo "Running Camera Calibration Toolbox GUI with virtual display..."
echo "This will start the GUI in a virtual framebuffer (no visible window)"
echo ""

cd "$(dirname "$0")"
source .venv/bin/activate

# Run with Xvfb for headless GUI testing
xvfb-run -a python Python/calib_gui.py

echo ""
echo "GUI test completed."

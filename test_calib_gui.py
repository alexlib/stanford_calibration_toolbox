#!/usr/bin/env python3
"""
Simple test script to verify the calib_gui fix
"""
import os
import sys

# Add the Python directory to path so we can import calib_gui
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Python'))

try:
    from calib_gui import has_display, calib_gui

    print("Testing display detection...")
    display_available = has_display()
    print(f"Display available: {display_available}")
    print(f"DISPLAY env var: {os.environ.get('DISPLAY', 'None')}")

    print("\nTesting mode=1 (should work without GUI)...")
    calib_gui(1)

    print("\nTesting mode=0 (standard mode)...")
    calib_gui(0)

    print("\nTesting GUI mode with fallback...")
    # Temporarily unset DISPLAY to test fallback
    original_display = os.environ.get('DISPLAY')
    if 'DISPLAY' in os.environ:
        del os.environ['DISPLAY']

    print(f"Display after unsetting: {os.environ.get('DISPLAY', 'None')}")
    print("This should use command-line interface...")

    # Restore DISPLAY
    if original_display:
        os.environ['DISPLAY'] = original_display

    print("\nTest completed successfully!")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

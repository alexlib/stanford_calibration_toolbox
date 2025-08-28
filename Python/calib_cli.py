#!/usr/bin/env python3
"""
Simple command-line interface for Camera Calibration Toolbox
This version completely avoids GUI/tkinter to prevent XCB issues
"""
import sys

def standard_mode():
    """Run the standard calibration mode (all images stored in memory)"""
    print("Running standard calibration mode...")
    print("TODO: Implement calib_gui_normal functionality")
    print("For now, this is a placeholder")

def memory_efficient_mode():
    """Run the memory efficient calibration mode (images loaded one by one)"""
    print("Running memory efficient calibration mode...")
    print("TODO: Implement calib_gui_no_read functionality")
    print("For now, this is a placeholder")

def exit_app():
    """Exit the application"""
    print("Bye. To run again, type: python Python/calib_cli.py")

def command_line_interface():
    """Command-line interface - no GUI dependencies"""
    print("\nCamera Calibration Toolbox - Select mode of operation:")
    print("1. Standard (all the images are stored in memory)")
    print("2. Memory efficient (the images are loaded one by one)")
    print("3. Exit")

    while True:
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            if choice == '1':
                standard_mode()
                break
            elif choice == '2':
                memory_efficient_mode()
                break
            elif choice == '3':
                exit_app()
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except EOFError:
            print("\nExiting...")
            break

def calib_cli(mode=None):
    """
    Command-line version of Camera Calibration Toolbox.
    Set mode to 1 to run the memory efficient version.
    Any other value for mode will run the normal version.

    Args:
        mode (int, optional): Mode of operation. If None, shows CLI menu.
    """
    if mode is None:
        print("Camera Calibration Toolbox (Command Line Interface)")
        print("This version avoids all GUI dependencies for maximum compatibility.")
        command_line_interface()
    else:
        if not isinstance(mode, (int, str)):
            mode = 0
        elif isinstance(mode, str):
            try:
                mode = int(mode)
            except ValueError:
                mode = 0

        if mode == 1:
            memory_efficient_mode()
        else:
            standard_mode()

if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        calib_cli(mode)
    else:
        calib_cli()

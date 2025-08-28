import sys
import os

def standard_mode():
    """Run the standard calibration mode (all images stored in memory)"""
    print("Running standard calibration mode...")
    # TODO: Implement calib_gui_normal functionality
    # For now, this is a placeholder

def memory_efficient_mode():
    """Run the memory efficient calibration mode (images loaded one by one)"""
    print("Running memory efficient calibration mode...")
    # TODO: Implement calib_gui_no_read functionality
    # For now, this is a placeholder

def exit_app():
    """Exit the application"""
    print("Bye. To run again, type calib_gui.")

def command_line_interface():
    """Command-line interface"""
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

def create_window():
    """Create the main GUI window"""
    print("Attempting to start GUI...")
    print("Note: If you see XCB errors, use command-line mode instead.")
    print("You can also try: xvfb-run -a python Python/calib_gui.py --gui")

    try:
        # Set environment variable to try to avoid XCB threading issues
        os.environ['XLIB_SKIP_ARGB_VISUALS'] = '1'

        import tkinter as tk
        global root
        root = tk.Tk()
        root.title("Camera Calibration Toolbox - Select mode of operation:")
        root.geometry("400x150")  # Set window size
        root.resizable(False, False)  # Make window non-resizable

        # Create buttons
        btn_standard = tk.Button(
            root,
            text="Standard (all the images are stored in memory)",
            command=standard_mode,
            width=50,
            height=2
        )
        btn_standard.pack(pady=5)

        btn_memory = tk.Button(
            root,
            text="Memory efficient (the images are loaded one by one)",
            command=memory_efficient_mode,
            width=50,
            height=2
        )
        btn_memory.pack(pady=5)

        btn_exit = tk.Button(
            root,
            text="Exit",
            command=exit_app,
            width=50,
            height=2
        )
        btn_exit.pack(pady=5)

        root.mainloop()
    except Exception as e:
        print(f"GUI Error: {e}")
        print("Falling back to command-line interface...")
        command_line_interface()

def calib_gui(mode=None):
    """
    Runs the Camera Calibration Toolbox.
    Set mode to 1 to run the memory efficient version.
    Any other value for mode will run the normal version.

    Args:
        mode (int, optional): Mode of operation. If None, shows GUI or CLI.
    """
    if mode is None:
        # Default to command-line interface to avoid XCB issues
        print("Using command-line interface (GUI may have display issues).")
        print("To force GUI attempt, use: python Python/calib_gui.py --gui")
        command_line_interface()
    else:
        if not isinstance(mode, (int, str)):
            mode = 0
        elif isinstance(mode, str):
            if mode == "--gui":
                create_window()
                return
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
        calib_gui(mode)
    else:
        calib_gui()

#!/usr/bin/env python3
"""
Test script to verify Tkinter works in the conda environment
"""
import tkinter as tk
import sys
import os

def test_tkinter():
    """Test basic Tkinter functionality"""
    try:
        print("Testing Tkinter in conda environment...")

        # Create main window
        root = tk.Tk()
        root.title("Conda Tkinter Test")
        root.geometry("300x150")

        # Add a label
        label = tk.Label(root, text="Tkinter works in conda!", font=("Arial", 14))
        label.pack(pady=20)

        # Add a button to close
        button = tk.Button(root, text="Close", command=root.quit)
        button.pack(pady=10)

        print("✅ Tkinter window created successfully!")
        print("✅ GUI test completed - Tkinter is working properly")

        # For automated testing, we'll close immediately
        # In a real scenario, you'd call root.mainloop()
        root.after(100, root.quit)  # Close after 100ms
        root.mainloop()

        return True

    except Exception as e:
        print(f"❌ Tkinter test failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing Tkinter in conda environment...")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}")

    success = test_tkinter()
    if success:
        print("\n🎉 SUCCESS: Tkinter is working properly in the conda environment!")
        print("You can now run GUI applications without XCB errors.")
    else:
        print("\n❌ FAILURE: Tkinter is not working properly.")
        sys.exit(1)

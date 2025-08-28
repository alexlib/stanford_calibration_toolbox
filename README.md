# Learning Calibraton by translating the Camera Calibration Toolbox for Matlab to Python

Camera Calibration Toolbox for Matlab, preserved by Stanford [Link](https://robots.stanford.edu/cs223b04/JeanYvesCalib/)

### Some of this code is based on the original Matlab code by Jean-Yves Bouguet

http://www.vision.caltech.edu/bouguetj/calib_doc/

### The paper about the Zhang's method is here:

[PDF](tr98-71.pdf)

## Python Environment Setup

This project uses `conda` for Python environment management, which provides better compatibility with GUI libraries like Tkinter.

### Prerequisites
- Install `conda` if not already installed (Miniforge recommended):
  ```bash
  # Download and install Miniforge
  wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
  bash Miniforge3-Linux-x86_64.sh
  ```

### Environment Setup
A conda environment named `calibration_toolbox` has been created with Python 3.11 and Tkinter support.

### Automatic Activation (VS Code)
When opening this project in VS Code, the conda environment will be automatically activated due to the `.vscode/settings.json` configuration.

### Manual Activation
If you need to activate the environment manually:
```bash
# Using the provided script
./activate_venv.sh

# Or directly with conda
conda activate calibration_toolbox
```

## Camera Calibration GUI

The Python implementation includes both GUI and command-line interfaces that replicate the MATLAB interface.

### Running the Application

#### Option 1: GUI Mode (Now Working!)
With the conda environment, Tkinter GUI works properly:

```bash
# Activate environment
conda activate calibration_toolbox

# Run GUI (recommended)
python Python/calib_gui.py --gui

# Or run interactive mode (will show GUI)
python Python/calib_gui.py
```

#### Option 2: Command Line Interface
For headless environments or when GUI is not needed:

```bash
# Activate environment
conda activate calibration_toolbox

# Run CLI version
python Python/calib_cli.py

# Run with specific mode
python Python/calib_cli.py 1  # Memory efficient mode
python Python/calib_cli.py 0  # Standard mode
```

#### Option 3: Direct Mode Parameters
```bash
# Activate environment
conda activate calibration_toolbox

# Run with specific mode (works with both scripts)
python Python/calib_gui.py 1  # Memory efficient mode
python Python/calib_cli.py 1  # Same result, CLI version
```

### Current Status
- ✅ **GUI Mode**: Working properly with conda environment
- ✅ **Command-line interface**: Fully functional and stable
- ✅ **Mode parameters**: Working perfectly
- ✅ **Tkinter**: Properly configured in conda environment
- ✅ **No XCB errors**: Resolved with conda environment setup

### Files
- `Python/calib_cli.py`: Pure command-line interface (no GUI dependencies)
- `Python/calib_gui.py`: GUI-capable with Tkinter support
- `test_tkinter.py`: Test script to verify GUI functionality
- `run_gui.sh`: Script for testing GUI with virtual display (if needed)

### Future connection to OpenPTV:
[OpenPTV](http://openptv.net/)
[GitHub](https://github.com/openptv/openptv-python)
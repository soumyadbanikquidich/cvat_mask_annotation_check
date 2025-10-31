# YOLO Segmentation Mask Verification Tool

This tool helps you verify segmentation masks from CVAT annotations that are in the YOLO segmentation format. It creates visualization images where only the segmented areas are visible against a black background, making it easy to verify the accuracy of your annotations.


## Features

- Works with YOLO segmentation format 1.0
- Supports both .jpg and .png images
- Creates visualizations with masked regions only
- Easy to use for non-technical users
- Works on any operating system (Windows/Mac/Linux)

## Prerequisites

Before you begin, make sure you have:

1. Python installed on your computer (version 3.7 or higher)
   - Download from: https://www.python.org/downloads/
   - During installation, make sure to check "Add Python to PATH"

## Getting Your Dataset Ready

1. Export your dataset from CVAT:
   - Open your project in CVAT
   - Click on "Actions" (three dots) for your task
   - Select "Export task Dataset"
   - Choose "YOLO" format
   - In the format settings, select "Ultralytics YOLO Segmentation 1.0"
   - Put your custom dataset name
   - Click "OK" to download
   - Extract the downloaded ZIP file

2. Place your dataset:
   - Extract the downloaded CVAT export
   - Move or copy the extracted dataset folder to your code directory
   - The dataset should contain `images/train/` and `labels/train/` folders


## Dataset Structure

Your dataset should be organized in the following structure:
```
your_dataset_folder/
├── data.yaml
├── images/
│   └── train/
│       └── (your image files .jpg or .png)
└── labels/
    └── train/
        └── (your label files .txt)
```

## Installation (Windows-specific Instructions)

1. Get the code (two options):

   Option 1 - Clone the repository (Recommended):
   ```
   git clone https://github.com/soumyadbanikquidich/cvat_mask_annotation_check.git
   cd cvat_mask_annotation_check
   ```

   Option 2 - If git is not installed or clone doesn't work:
   - Click the green "Code" button above
   - Select "Download ZIP"
   - Right-click the downloaded ZIP file and select "Extract All"
   - Choose a location you can easily access (e.g., `C:\Users\YourUsername\Documents`)

2. Install Python (if not already installed):
   - Go to https://www.python.org/downloads/windows/
   - Download the latest Python installer (e.g., Python 3.12)
   - Run the installer
   - **IMPORTANT**: Check the box that says "Add Python to PATH" during installation
   - Click "Install Now"

3. Open Command Prompt as Administrator:
   - Press the Windows key
   - Type "cmd"
   - Right-click on "Command Prompt"
   - Select "Run as administrator"

4. Navigate to your tool's directory (example):
   ```
   cd C:\Users\YourUsername\Documents\cvat_mask_annotation_check
   ```
   (Replace `YourUsername` with your actual Windows username)

5. Install required packages:
   ```
   pip install -r requirements.txt
   ```

Note: If you see any "Access denied" errors, make sure you're running Command Prompt as Administrator.

## Usage (Windows)

1. Open `verify_masks.py`:
   - Right-click on `verify_masks.py`
   - Select "Edit with Notepad" or "Open with" → "Notepad" or any code editor e.g. vscode

2. Modify these two lines at the bottom of the file with your Windows paths:
   ```python
   dataset_dir = r"C:\Users\YourUsername\your_dataset_folder"  # Change this
   output_dir = r"C:\Users\YourUsername\destination path\masked_output"         # Change this
   ```
   - Make sure to use `\` (backslash) in Windows paths
   - Keep the `r` before the path string
   - Example real path: `r"C:\Users\Soumyadeep\Documents\my_yolo_dataset"`

3. Save the file:
   - Press Ctrl + S in Notepad
   - Close Notepad

4. Run the script:
   - Open Command Prompt (if not already open)
   - Navigate to the tool's directory
   - Run:
   ```
   python verify_masks.py
   ```

4. Check the output folder for the verification images:
   - Original images with only the masked areas visible
   - All other areas will be black
   - File names will be prefixed with "masked_"

## Example Output

Input Image | Verification Output
:----------:|:------------------:
Original image with full content | Same image with only masked regions visible

## Common Issues and Solutions (Windows)

1. **"Python not found" error**:
   - Verify Python installation:
     1. Open Command Prompt
     2. Type `python --version`
     3. If not found, reinstall Python and check "Add Python to PATH"
   - Alternative fix: Use full Python path
     ```
     C:\Users\YourUsername\AppData\Local\Programs\Python\Python312\python.exe verify_masks.py
     ```

2. **"Module not found" error**:
   - Open Command Prompt as Administrator
   - Run these commands:
     ```
     pip uninstall opencv-python numpy pyyaml
     pip install -r requirements.txt
     ```

3. **"No such file or directory" error**:
   - Check if your paths use correct Windows format:
     - Use `\` instead of `/`
     - Use full paths starting with `C:\`
     - Keep the `r` prefix before paths
   - Example correct path:
     ```python
     dataset_dir = r"C:\Users\Soumyadeep\Documents\dataset"
     ```

4. **"Permission denied" error**:
   - Run Command Prompt as Administrator
   - Check if antivirus is blocking Python
   - Make sure you have write permissions to the output folder

5. **"Invalid syntax" error in paths**:
   - Make sure you're using raw strings with `r` prefix
   - Don't use single backslashes without `r` prefix
   - Correct: `r"C:\Users\Soumyadeep"`
   - Also correct: `"C:\\Users\\Soumyadeep"`

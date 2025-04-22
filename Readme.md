 ## Description
 This Python script organizes files in a specified directory into folders based on their file type (e.g., Images, Documents, Videos). It uses the `os` and `shutil` libraries to manage file operations.
 
 ## Features
 - Automatically creates folders for Images, Documents, Videos, and Others.
 - Moves files to the appropriate folder based on their extension.
 - Handles unknown file types by moving them to an "Others" folder.
 
 ## How to Use
 1. Install Python 3.7 or higher.
 2. Place the script in the desired directory.
 3. Update the `target_directory` variable in the script to the path of the folder you want to organize.
 4. Run the script using: `python file_organizer.py`.
 
 ## Example
 Before: Files like `photo.jpg`, `doc.pdf`, `clip.mp4` are in a single folder.
 After: Files are moved to `Images`, `Documents`, `Videos`, or `Others` folders.
 

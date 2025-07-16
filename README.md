File Organizer Script
======================

This script organizes files from your Downloads folder into categorized subfolders 
based on file extensions such as Images, Videos, Documents, and Others.

Features
--------
- Automatically sorts files by type
- Categorizes into: Images, Videos, Documents, Others
- Logs all file movements and errors
- Creates required folders if they don't exist

Requirements
------------
- Python 3.x
- No external libraries required (uses os, shutil, logging)

Setup
-----
1. Make sure Python 3 is installed.
2. Save the script as `file_organizer.py`.
3. (Optional) Modify the `SOURCE_DIR` in the script if you want to organize a different folder:
   SOURCE_DIR = os.path.join(os.path.expanduser("~"), "Downloads")

How to Run
----------
Open a terminal or command prompt and run:

    python file_organizer.py

What It Does
------------
- Moves files into:
  Downloads/
  └── organized_downloads/
      ├── Documents/
      ├── Images/
      ├── Videos/
      └── Others/
- Supported extensions:
  - Images: .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp
  - Videos: .mp4, .mkv, .mov, .avi, .flv, .wmv
  - Documents: .pdf, .docx, .doc, .pptx, .ppt, .xlsx, .xls, .txt, .csv, .zip, .rar
  - Others: Anything not matching the above

Logging
-------
- Log file is saved as:
  Downloads/organized_downloads/file_organizer.log
- Logs include moved files and any errors encountered

Author
------
Code by: M. Shameer Asim

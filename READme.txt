============================================================
           MULTI-THREADED FILE COPIER (v1.0)
============================================================

DESCRIPTION:
This is a lightweight Graphical User Interface (GUI) 
application built with Python to handle file copying 
tasks efficiently. By utilizing Multi-threading, the 
application ensures that the window remains responsive 
even when moving large amounts of data.

FEATURES:
- Responsive UI: No "Not Responding" lag during copy.
- Progress Tracking: Visual Progress Bar and file count.
- Recursive Copying: Copies all files and subfolders.
- Error Handling: Validates paths before starting.

REQUIREMENTS:
- Python 3.x
- Tkinter library (Included in standard Python)

HOW TO USE:
1. Run the script: python3 Thread_copy.py => Linux
                   python Thread_copy.py  => windows
2. Enter the 'Source Path' (Folder to copy from).
3. Enter the 'Destination Path' (Folder to copy to).
4. Click 'Copy' to begin the process.
5. Wait for the 'Success' notification.

TECHNICAL DETAILS:
- Language: Python
- GUI Framework: Tkinter
- Concurrency: ThreadPoolExecutor
- File Operations: OS & Shutil

DEVELOPED BY:
[ prazad-21 ]
Date: January 2026
============================================================

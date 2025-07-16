import os
import shutil
import logging

SOURCE_DIR = os.path.join(os.path.expanduser("~"), "Downloads")
TARGET_DIR = os.path.join(SOURCE_DIR, "organized_downloads")
LOG_FILE = os.path.join(TARGET_DIR, "file_organizer.log")

# Categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv"],
    "Documents": [".pdf", ".docx", ".doc", ".pptx", ".ppt", ".xlsx", ".xls", ".txt", ".csv", ".zip", ".rar"],
}
CATEGORIES["Others"] = [] 

os.makedirs(TARGET_DIR, exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s — %(levelname)s — %(message)s',
)

for category in CATEGORIES:
    os.makedirs(os.path.join(TARGET_DIR, category), exist_ok=True)

for filename in os.listdir(SOURCE_DIR):
    file_path = os.path.join(SOURCE_DIR, filename)

    if os.path.isfile(file_path) and file_path != LOG_FILE:
        ext = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in CATEGORIES.items():
            if category != "Others" and ext in extensions:
                try:
                    dest = os.path.join(TARGET_DIR, category, filename)
                    shutil.move(file_path, dest)
                    logging.info(f"Moved: {filename} → {category}")
                except Exception as e:
                    logging.error(f"Failed to move {filename}: {e}")
                moved = True
                break

        if not moved:
            try:
                dest = os.path.join(TARGET_DIR, "Others", filename)
                shutil.move(file_path, dest)
                logging.info(f"Moved: {filename} → Others")
            except Exception as e:
                logging.error(f"Failed to move {filename}: {e}")

print("✅ Files sorted into organized_downloads/[Images, Videos, Documents, Others]. Logs saved.")


#code by: M. Shameer Asim
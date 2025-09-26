import argparse
import os
import glob
import platform
import psutil
from datetime import datetime

# -------------------- SEARCH FILES --------------------
def search_files(pattern, path="."):
    print(f"🔍 Searching for files matching '{pattern}' in {path}...")
    files = glob.glob(os.path.join(path, pattern), recursive=True)
    if files:
        for f in files:
            print(f"📁 {f}")
    else:
        print("❌ No files found.")
    return files

# -------------------- BATCH RENAME --------------------
def batch_rename(path, prefix=None, suffix=None):
    if not os.path.isdir(path):
        print("❌ Invalid path.")
        return

    files = os.listdir(path)
    for idx, filename in enumerate(files, start=1):
        old_path = os.path.join(path, filename)
        if os.path.isfile(old_path):
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix or ''}{name}{suffix or ''}{ext}"
            new_path = os.path.join(path, new_name)
            os.rename(old_path, new_path)
            print(f"✏️ Renamed: {filename} ➝ {new_name}")

# -------------------- SYSTEM INFO --------------------
def get_system_info():
    print("\n🖥️ System Information:")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"RAM Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")

# -------------------- MAIN --------------------
def main():
    parser = argparse.ArgumentParser(
        description="🤖 CLI Chatbot: Automate tasks like searching, renaming, and system info."
    )

    parser.add_argument("--search", help="Search files by pattern (e.g., '*.txt')")
    parser.add_argument("--path", help="Directory path to search or rename", default=".")
    parser.add_argument("--rename", action="store_true", help="Batch rename files")
    parser.add_argument("--prefix", help="Add prefix while renaming")
    parser.add_argument("--suffix", help="Add suffix while renaming")
    parser.add_argument("--sysinfo", action="store_true", help="Display system info")

    args = parser.parse_args()

    if args.search:
        search_files(args.search, args.path)

    if args.rename:
        batch_rename(args.path, args.prefix, args.suffix)

    if args.sysinfo:
        get_system_info()

    if not any([args.search, args.rename, args.sysinfo]):
        parser.print_help()

if __name__ == "__main__":
    main()

import os
import hashlib

def get_file_hash(file_path):
    """Compute SHA256 hash of a file in chunks."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(directory):
    """Find duplicate files in a directory by comparing hashes."""
    hashes = {}
    duplicates = {}

    for root, _, files in os.walk(directory):
        print(f"🔍 Scanning {root}...")
        print(f"   Found {len(files)} files.",files)
        print("   Computing hashes...", _)
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_hash = get_file_hash(file_path)
                if file_hash in hashes:
                    duplicates.setdefault(file_hash, [hashes[file_hash]]).append(file_path)
                else:
                    hashes[file_hash] = file_path
            except Exception as e:
                print(f"⚠ Could not hash {file_path}: {e}")
    print(hashes)
    print(duplicates)
    return duplicates

def print_duplicates(duplicates):
    if not duplicates:
        print("✅ No duplicates found.")
        return

    print("\n🔎 Duplicate files detected:")
    for file_hash, files in duplicates.items():
        print(f"\nSHA256: {file_hash}")
        for f in files:
            print(f" - {f}")

def delete_duplicates(duplicates):
    """Ask user if they want to delete duplicate files."""
    for file_hash, files in duplicates.items():
        print(f"\nSHA256: {file_hash}")
        for idx, f in enumerate(files, 1):
            print(f" {idx}. {f}")
        keep = input("👉 Enter number of file to keep (others will be deleted): ")
        try:
            keep = int(keep)
            for idx, f in enumerate(files, 1):
                if idx != keep:
                    os.remove(f)
                    print(f"🗑 Deleted: {f}")
        except (ValueError, IndexError):
            print("❌ Invalid choice. Skipping this group.")

if __name__ == "__main__":
    folder = input("📂 Enter the directory path to scan: ").strip()
    duplicates = find_duplicates(folder)
    print_duplicates(duplicates)

    if duplicates:
        choice = input("\n❓ Do you want to delete duplicates? (y/n): ").lower()
        if choice == "y":
            delete_duplicates(duplicates)

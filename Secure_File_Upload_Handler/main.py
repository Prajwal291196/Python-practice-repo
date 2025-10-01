import os
import uuid
import hashlib
from flask import Flask, request, jsonify, abort
from werkzeug.utils import secure_filename
from pathlib import Path

# --------- CONFIGURATION ---------
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Make upload dir more restrictive (owner rwx, group+others none) - note: on Windows this is ignored
UPLOAD_DIR.chmod(0o700)

# Allowed extensions (lowercase)
ALLOWED_EXTENSIONS = {
    "png", "jpg", "jpeg", "gif", "pdf", "txt", "csv"
}

# Max size in bytes (example: 10 MB)
MAX_CONTENT_LENGTH = 10 * 1024 * 1024

# Flask app
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH


# --------- HELPERS ---------
def allowed_extension(filename: str) -> bool:
    if "." not in filename:
        return False
    ext = filename.rsplit(".", 1)[1].lower()
    return ext in ALLOWED_EXTENSIONS


def file_signature_ok(stream, filename: str) -> bool:
    """
    Basic file signature checks for common types.
    Reads a few bytes from the stream and checks known signatures.
    This is not exhaustive but protects against simple extension spoofing.
    The stream position is reset to the beginning for saving later.
    """
    sig = stream.read(16)
    stream.seek(0)

    ext = filename.rsplit(".", 1)[1].lower() if "." in filename else ""

    # PNG: 89 50 4E 47 0D 0A 1A 0A
    if ext == "png" and sig.startswith(b"\x89PNG\r\n\x1a\n"):
        return True

    # JPEG: ff d8 ff
    if ext in {"jpg", "jpeg"} and sig.startswith(b"\xff\xd8\xff"):
        return True

    # GIF: GIF87a or GIF89a
    if ext == "gif" and (sig.startswith(b"GIF87a") or sig.startswith(b"GIF89a")):
        return True

    # PDF: %PDF-
    if ext == "pdf" and sig.startswith(b"%PDF-"):
        return True

    # Text, CSV - allow printable bytes (basic heuristic)
    if ext in {"txt", "csv"}:
        # If many null bytes, reject
        if b"\x00" in sig:
            return False
        return True

    # If extension is unknown but allowed enum included it, allow for now (best-effort)
    return ext in ALLOWED_EXTENSIONS


def generate_safe_filename(original_filename: str) -> str:
    """
    Create a unique filename using UUID and preserve extension.
    Use secure_filename to remove path characters.
    """
    original = secure_filename(original_filename)
    ext = original.rsplit(".", 1)[1].lower() if "." in original else ""
    unique = f"{uuid.uuid4().hex}"
    return f"{unique}.{ext}" if ext else unique


def compute_sha256(file_path: Path) -> str:
    h = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


# --------- ROUTES ---------
@app.route("/upload", methods=["POST"])
def upload_file():
    # check if the post request has the file part
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not allowed_extension(file.filename):
        return (
            jsonify({"error": "File type not allowed", "allowed": sorted(list(ALLOWED_EXTENSIONS))}),
            400,
        )

    # Basic content type check (trust but verify)
    content_type = file.content_type or ""
    # For stronger checking, map extension->expected mime and compare. We skip strict mapping here.

    # Basic signature check to reduce extension spoofing
    try:
        if not file_signature_ok(file.stream, file.filename):
            return jsonify({"error": "File signature does not match the extension or file is malformed"}), 400
    except Exception:
        return jsonify({"error": "Failed to inspect file signature"}), 400

    # Generate safe unique filename and save
    safe_name = generate_safe_filename(file.filename)
    destination = UPLOAD_DIR / safe_name

    try:
        # Save file to disk
        file.save(str(destination))

        # Set restrictive permissions for the file (owner rw only)
        try:
            destination.chmod(0o600)
        except Exception:
            # Non-unix systems may ignore chmod - ignore errors silently
            pass

        sha256 = compute_sha256(destination)

        return jsonify({
            "message": "File uploaded successfully",
            "filename": safe_name,
            "original_filename": file.filename,
            "sha256": sha256,
            "content_type": content_type,
            "size_bytes": destination.stat().st_size,
            "path": str(destination)
        }), 201

    except Exception as e:
        # If save failed, ensure no partial file remains
        if destination.exists():
            try:
                destination.unlink()
            except Exception:
                pass
        return jsonify({"error": "Failed to save file", "detail": str(e)}), 500


@app.errorhandler(413)
def too_large(e):
    return jsonify({"error": "File too large", "max_bytes": app.config["MAX_CONTENT_LENGTH"]}), 413


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "upload_dir": str(UPLOAD_DIR)})


# --------- RUN SERVER (for dev only) ---------
if __name__ == "__main__":
    # NEVER use Flask's reloader or debug mode in production for uploads + security.
    app.run(host="0.0.0.0", port=5000)

# python-file-manager
# 📂 Terminal-Based File Manager (Python)

A robust and user-friendly Command Line Interface (CLI) tool built with Python to manage files and directories. This project utilizes modern Python libraries like `pathlib` and `shutil` to ensure safe, cross-platform filesystem operations.

## ✨ Features

- **Folder Management**: 
  - Create new directories.
  - Rename existing folders.
  - **Recursive Delete**: Automatically handles non-empty folders (using `shutil.rmtree`).
- **File Management**:
  - Create new files with custom content.
  - Read file contents directly in the terminal.
  - Delete files securely.
- **File Updates**:
  - Rename files.
  - Append new data to existing files.
  - Overwrite file content.
- **Real-time Listing**: View all items in the current directory with labels `[File]` or `[Folder]`.
- **Error Handling**: Comprehensive `try-except` blocks to prevent crashes from invalid inputs or system errors.

## 🛠️ Technologies Used

- **Language**: Python 3.x
- **Core Modules**:
  - `pathlib`: For object-oriented filesystem paths.
  - `shutil`: For high-level file operations (deleting non-empty trees).
  - `os`: For basic operating system interactions.

## 🚀 Getting Started

### Prerequisites
Ensure you have Python 3 installed. Check by running:
```bash
python --version

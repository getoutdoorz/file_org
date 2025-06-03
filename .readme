# File Organization Tool

A Python script that automatically organizes files in a directory by their file extensions, creating subdirectories for each extension type.

## Features

- **Organize files**: Groups files by extension into directories prefixed with "_" (e.g., `_py`, `_txt`, `_jpg`)
- **Reverse organization**: Move files back from extension directories to the main directory
- **ASCII tree display**: Shows the directory structure after organization
- **Command-line interface**: Easy to use with arguments and options
- **Cross-platform**: Uses os.path.join() for proper path handling

## Requirements

- Python 3.x
- Standard library only (no external dependencies)

## Installation

1. Clone or download the script
2. Make it executable: `chmod +x organizeDir.py`
3. Optionally, copy to your PATH: `cp organizeDir.py ~/bin/organizeDir` & `source ~/.zshrc`

## Usage

### Basic organization
```bash
# Organize current directory
python organizeDir.py

# Organize specific directory
python organizeDir.py /path/to/directory
python organizeDir.py myFolder
```

### Reverse organization
```bash
# Reverse organization in current directory
python organizeDir.py -r

# Reverse organization in specific directory
python organizeDir.py -r myFolder
python organizeDir.py --reverse /path/to/directory
```

### Help
```bash
python organizeDir.py --help
```

## Example

Before organization:
```
my_folder/
├── document.pdf
├── image.jpg
├── script.py
├── README
└── data.csv
```

After running `python organizeDir.py my_folder`:
```
my_folder/
├── _csv/
│   └── data.csv
├── _jpg/
│   └── image.jpg
├── _no_extension/
│   └── README
├── _pdf/
│   └── document.pdf
└── _py/
    └── script.py
```

## File Handling

- Files with extensions are moved to directories named `_<extension>` (e.g., `_py`, `_txt`)
- Files without extensions are moved to `_no_extension`
- Existing directories are preserved and not moved
- Extension directories are automatically created as needed

## Testing

Run the test suite:
```bash
python test.py
```

## Notes

- The script creates directories with "_" prefix to clearly identify them as extension-based folders
- Use the reverse option (-r) to undo organization and restore the original structure
- The ASCII tree display shows up to 3 directory levels for clarity

# AGENT.md

## Project: Python File Organization Tool

### Commands
- **Test**: `python -m pytest test.py` or `python test.py`
- **Run main script**: `python organizeDir.py`
- **Lint**: `python -m flake8 *.py` or `python -m pylint *.py`
- **Type check**: `python -m mypy *.py`

### Code Style Guidelines
- **Language**: Python 3
- **Imports**: Standard library imports first, third-party after blank line
- **Functions**: Use snake_case naming, include docstrings with Inputs/Outputs/Description format
- **Variables**: Use snake_case (e.g., `file_path`, `ext_dir`, `extList`)
- **Comments**: Use `#` for inline comments explaining logic
- **Error handling**: Use if/else checks for path validation and file operations
- **File operations**: Use `os.path.join()` for cross-platform paths, `os.path.exists()` for validation
- **String formatting**: Use f-strings when needed, simple concatenation for paths via `os.path.join()`
- **Main function**: Always include `if __name__ == "__main__":` guard

### Project Structure
- Main script: `organizeDir.py` - organizes files by extension into subdirectories
- Test file: `test.py` - currently empty, add tests here
- Uses standard library only: `os`, `shutil`

#!/usr/bin/env python3
import os
import shutil
import argparse

def organize_by_extension(path):
    """
    Inputs: A path name (string) to the directory to organize.
    Outputs: None
    Description: Organizes a directory into subdirectories for each file name extension type.
    """
    files = os.listdir(path)
    extList = []

    if files:
        for file in files:
            # get full file path
            file_path = os.path.join(path, file)

            # skip step if file is dir
            if os.path.isdir(file_path):
                continue

            # split file name by extension
            root, ext = os.path.splitext(file)

            # if no ext, put in special folder
            if ext == '':
                ext = 'no_extension'
                ext_name = '_no_extension'
            else:
                ext_name = "_" + ext.replace('.', '')
            
            ext_dir = os.path.join(path, ext_name)
            if ext not in extList:
                extList.append(ext)
                if not os.path.exists(ext_dir):
                    os.mkdir(ext_dir)

            # move file to ext dir
            shutil.move( file_path, os.path.join(ext_dir, file) )

def reverse_organization(path):
    """
    Inputs: A path name (string) to the directory to reverse organization.
    Outputs: None
    Description: Reverses file organization by moving files from extension directories back to main directory.
    """
    items = os.listdir(path)
    
    for item in items:
        item_path = os.path.join(path, item)
        
        # Check if it's a directory that starts with "_" (extension directory)
        if os.path.isdir(item_path) and (item.startswith('_') or item == 'no_extension'):
            print(f"Processing directory: {item}")
            
            # Move all files from this directory back to parent
            try:
                files_in_dir = os.listdir(item_path)
                for file in files_in_dir:
                    file_path = os.path.join(item_path, file)
                    if os.path.isfile(file_path):
                        shutil.move(file_path, os.path.join(path, file))
                        print(f"  Moved: {file}")
                
                # Remove the empty directory
                os.rmdir(item_path)
                print(f"  Removed directory: {item}")
                
            except OSError as e:
                print(f"  Error processing {item}: {e}")

def display_tree(path, prefix="", is_last=True, max_depth=3, current_depth=0):
    """
    Inputs: A path to display, prefix for formatting, is_last flag, max_depth, current_depth
    Outputs: None (prints tree structure)
    Description: Displays directory structure in ASCII tree format
    """
    if current_depth > max_depth:
        return
    
    basename = os.path.basename(path) or path
    connector = "└── " if is_last else "├── "
    print(f"{prefix}{connector}{basename}")
    
    if os.path.isdir(path) and current_depth < max_depth:
        try:
            items = sorted(os.listdir(path))
            # Separate directories and files, directories first
            dirs = [item for item in items if os.path.isdir(os.path.join(path, item))]
            files = [item for item in items if os.path.isfile(os.path.join(path, item))]
            all_items = dirs + files
            
            for i, item in enumerate(all_items):
                item_path = os.path.join(path, item)
                is_last_item = i == len(all_items) - 1
                extension = "    " if is_last else "│   "
                display_tree(item_path, prefix + extension, is_last_item, max_depth, current_depth + 1)
        except PermissionError:
            pass

def main():
    parser = argparse.ArgumentParser(description="Organize files by extension into subdirectories")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to organize (default: current directory)")
    parser.add_argument("-r", "--reverse", action="store_true", help="Reverse organization (move files back from extension directories)")
    args = parser.parse_args()
    
    myPath = args.directory
    if os.path.exists(myPath) and os.path.isdir(myPath):
        if args.reverse:
            reverse_organization(myPath)
            print("Reverse organization complete!")
        else:
            organize_by_extension(myPath)
            print("Organization Complete!")
        
        print("\nDirectory structure:")
        display_tree(myPath)
    else:
        print("Not a valid path or directory.")
    
if __name__ == "__main__":
    main()
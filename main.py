from pathlib import Path
import shutil
import os

# --- Helper Function to List Items ---
def list_items():
    print("\n--- Current Files and Folders ---")
    p = Path(".")
    items = list(p.glob('*')) # rglob('*') ki jagah glob('*') use kiya hai taaki sirf current folder dikhe (saaf dikhta hai)
    if not items:
        print("Empty Directory")
    for i, item in enumerate(items):
        type_str = "Folder" if item.is_dir() else "File"
        print(f"{i+1}: {item} [{type_str}]")
    print("---------------------------------")

# --- Folder Operations ---
def create_folder():
    try:
        name = input("Enter new folder name: ")
        p = Path(name)
        p.mkdir(exist_ok=True) # Agar pehle se ho toh error nahi dega
        print(f"Folder '{name}' created successfully.")
    except Exception as err:
        print(f"Error: {err}")

def update_folder():
    try:
        list_items()
        old_name = input("Enter the folder name to rename: ")
        p = Path(old_name)
        if p.exists() and p.is_dir():
            new_name = input("Enter new name: ")
            p.rename(Path(new_name))
            print("Folder renamed successfully.")
        else:
            print("Folder not found.")
    except Exception as err:
        print(f"Error: {err}")

def delete_folder():
    try:
        list_items()
        name = input("Enter folder name to delete (ALL contents will be deleted): ")
        p = Path(name)
        if p.exists() and p.is_dir():
            # IMPORTANT: shutil.rmtree non-empty folders ko delete karta hai
            shutil.rmtree(p)
            print(f"Folder '{name}' deleted successfully.")
        else:
            print("No such folder exists.")
    except Exception as err:
        print(f"Error: {err}")

# --- File Operations ---
def create_file():
    try:
        name = input("Enter file name (with extension, e.g., test.txt): ")
        p = Path(name)
        if not p.exists():
            data = input("Enter content for the file: ")
            p.write_text(data) # Pathlib ka asan tareeka
            print("File created successfully.")
        else:
            print("File already exists.")
    except Exception as err:
        print(f"Error: {err}")

def read_file():
    try:
        list_items()
        name = input("Enter the file name to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("\n--- File Content ---")
            print(p.read_text())
            print("--------------------")
        else:
            print("File not found.")
    except Exception as err:
        print(f"Error: {err}")

def update_file():
    try:
        list_items()
        name = input("Enter file name to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("1. Rename | 2. Append | 3. Overwrite")
            choice = input("Choice: ")
            
            if choice == '1':
                new_name = input("Enter new file name: ")
                p.rename(Path(new_name))
                print("File renamed.")
            elif choice == '2':
                data = input("Enter data to append: ")
                with open(p, 'a') as f:
                    f.write("\n" + data)
                print("Data appended.")
            elif choice == '3':
                data = input("Enter new content: ")
                p.write_text(data)
                print("File overwritten.")
        else:
            print("File not found.")
    except Exception as err:
        print(f"Error: {err}")

def delete_file():
    try:
        list_items()
        name = input("Enter file name to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("File deleted.")
        else:
            print("File not found.")
    except Exception as err:
        print(f"Error: {err}")

# --- Main Menu Loop ---
while True:
    print("\n========= FILE MANAGER =========")
    print("1. Create Folder   2. List All       3. Update Folder   4. Delete Folder")
    print("5. Create File     6. Read File       7. Update File     8. Delete File")
    print("0. Exit")
    
    try:
        choice = input("\nSelect Option: ")
        
        if choice == '1': create_folder()
        elif choice == '2': list_items()
        elif choice == '3': update_folder()
        elif choice == '4': delete_folder()
        elif choice == '5': create_file()
        elif choice == '6': read_file()
        elif choice == '7': update_file()
        elif choice == '8': delete_file()
        elif choice == '0':
            print("Exiting... Bye!")
            break
        else:
            print("Invalid Choice! Try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
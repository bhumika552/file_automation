import os
import shutil
import logging

# Configure logging
logging.basicConfig(
    filename="file_automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def rename_files(folder_path, prefix):
    try:
        files = os.listdir(folder_path)
        for i, file in enumerate(files):
            old_path = os.path.join(folder_path, file)
            if os.path.isfile(old_path):
                extension = os.path.splitext(file)[1]
                new_name = f"{prefix}_{i}{extension}"
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
                logging.info(f"Renamed: {file} → {new_name}")
        print("✅ Files renamed successfully.")
    except Exception as e:
        logging.error(f"Error in renaming files: {e}")
        print("❌ Error occurred while renaming files.")


def sort_files(folder_path):
    try:
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):
                extension = file.split('.')[-1]
                ext_folder = os.path.join(folder_path, extension)

                if not os.path.exists(ext_folder):
                    os.makedirs(ext_folder)

                shutil.move(file_path, os.path.join(ext_folder, file))
                logging.info(f"Moved: {file} → {extension}/")

        print("✅ Files sorted successfully.")
    except Exception as e:
        logging.error(f"Error in sorting files: {e}")
        print("❌ Error occurred while sorting files.")


def delete_files(folder_path, extension):
    try:
        files = os.listdir(folder_path)
        for file in files:
            if file.endswith(extension):
                os.remove(os.path.join(folder_path, file))
                logging.info(f"Deleted: {file}")

        print(f"✅ All .{extension} files deleted.")
    except Exception as e:
        logging.error(f"Error in deleting files: {e}")
        print("❌ Error occurred while deleting files.")


def main():
    while True:
        print("\n📌 File Automation Menu")
        print("1. Rename Files")
        print("2. Sort Files")
        print("3. Delete Files by Extension")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            path = input("Enter folder path: ")
            prefix = input("Enter prefix: ")
            rename_files(path, prefix)

        elif choice == '2':
            path = input("Enter folder path: ")
            sort_files(path)

        elif choice == '3':
            path = input("Enter folder path: ")
            ext = input("Enter extension (e.g., txt): ")
            delete_files(path, ext)

        elif choice == '4':
            print("👋 Exiting program.")
            break

        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
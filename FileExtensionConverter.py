import os

def change_extension_in_directory(directory, old_extension, new_extension):
    for root, _, files in os.walk(directory):
        print("root",root),
        print("files",files)
        for file in files:
            if file.endswith(old_extension):
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.splitext(old_file_path)[0] + new_extension
                os.rename(old_file_path, new_file_path)


directory_path = "C:\\Users\\sripa\\Documents\\temp"
old_extension = ".csv"  # Change to the extension you want to replace
new_extension = ".txt"  # Change to the new extension you want

change_extension_in_directory(directory_path, old_extension, new_extension)

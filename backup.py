# # # In DevOps, performing regular backups of important files is crucial:

# # # ●       Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.

# # # ●       The script should copy all files from the source directory to the destination directory.

# # # ●       Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.

# # # ●       Handle errors gracefully, such as when the source directory or destination directory does not exist.

# # # Sample Command:

# # # python backup.py /path/to/source /path/to/destination

# # # By running the script with the appropriate source and destination directories, it should create backups of the files in the source directory, ensuring unique file names in the destination directory.


# # import os
# # import shutil
# # import sys
# # import datetime

# # def backup_files(source_dir, destination_dir):
# #     """Back up files from source_dir to destination_dir with unique filenames."""
# #     if not os.path.exists(source_dir):
# #         print(f"Error: Source directory '{source_dir}' does not exist.")
# #         return
    
# #     if not os.path.exists(destination_dir):
# #         print(f"Destination directory '{destination_dir}' does not exist. Creating it now...")
# #         os.makedirs(destination_dir)
    
# #     for filename in os.listdir(source_dir):
# #         source_file = os.path.join(source_dir, filename)
# #         destination_file = os.path.join(destination_dir, filename)
        
# #         if os.path.isfile(source_file):
# #             if os.path.exists(destination_file):
# #                 timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
# #                 filename, ext = os.path.splitext(filename)
# #                 destination_file = os.path.join(destination_dir, f"{filename}_{timestamp}{ext}")
            
# #             shutil.copy2(source_file, destination_file)
# #             print(f"Copied: {source_file} -> {destination_file}")

# # if __name__ == "__main__":
# #     if len(sys.argv) != 3:
# #         print("Usage: python backup.py /path/to/source /path/to/destination")
# #         sys.exit(1)
    
# #     source_directory = sys.argv[1]
# #     destination_directory = sys.argv[2]
    
# #     backup_files(source_directory, destination_directory)

# # To run the script, use the following command:
# # python backup.py /path/to/source /path/to/destination
# # Replace /path/to/source and /path/to/destination with the actual source and destination directories.



# import os
# import shutil
# import datetime

# def backup_files(source_dir, destination_dir):
#     """Back up files from source_dir to destination_dir with unique filenames."""
#     if not os.path.exists(source_dir):
#         print(f"Error: Source directory '{source_dir}' does not exist.")
#         return
    
#     if not os.path.exists(destination_dir):
#         print(f"Destination directory '{destination_dir}' does not exist. Creating it now...")
#         os.makedirs(destination_dir)
    
#     for filename in os.listdir(source_dir):
#         source_file = os.path.join(source_dir, filename)
#         destination_file = os.path.join(destination_dir, filename)
        
#         if os.path.isfile(source_file):
#             if os.path.exists(destination_file):
#                 timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#                 filename, ext = os.path.splitext(filename)
#                 destination_file = os.path.join(destination_dir, f"{filename}_{timestamp}{ext}")
            
#             shutil.copy2(source_file, destination_file)
#             print(f"Copied: {source_file} -> {destination_file}")

# if __name__ == "__main__":
#     source_directory = input("Enter source directory: ")
#     destination_directory = input("Enter destination directory: ")
    
#     backup_files(source_directory, destination_directory)


import os
import shutil
import datetime

def backup_files(source_dir, destination_dir):
    """Back up files from source_dir to destination_dir with unique filenames."""
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    
    if not os.path.exists(destination_dir):
        print(f"Destination directory '{destination_dir}' does not exist. Creating it now...")
        os.makedirs(destination_dir)
    
    files_copied = 0
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)
        
        if os.path.isfile(source_file):
            if os.path.exists(destination_file):
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                filename, ext = os.path.splitext(filename)
                destination_file = os.path.join(destination_dir, f"{filename}_{timestamp}{ext}")
            
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {source_file} -> {destination_file}")
            files_copied += 1
    
    if files_copied > 0:
        print(f"Backup completed successfully. {files_copied} files copied.")
    else:
        print("No files were copied.")

if __name__ == "__main__":
    source_directory = input("Enter source directory: ")
    destination_directory = input("Enter destination directory: ")
    
    backup_files(source_directory, destination_directory)


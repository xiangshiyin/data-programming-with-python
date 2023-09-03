import argparse
import os

def create_folder_if_not_exist(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        print(f"Folder {folder_path} already exists.")
    else:
        os.mkdir(folder_path)
        print(f"Folder {folder_path} created")

def create_file_if_not_exist(file_path):
    if os.path.exists(file_path) and os.path.isfile(file_path):
        print(f"File {file_path} already exists")
    else:
        with open(file_path, "w") as file:
            pass
        print(f"File {file_path} created")


if __name__ == '__main__':
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Calculate the project's root directory by going up two levels
    project_root = os.path.abspath(os.path.join(script_dir, '..'))

    # Change the working directory to the project's root
    os.chdir(project_root)

    # Define arguments
    parser = argparse.ArgumentParser(description="This module is used to generate folders and files for every weekly class")
    parser.add_argument("--semester", type=str, required=True, help="Pick the semester folder")
    parser.add_argument("--week", type=str, help="Define the weekly folder name")

    # Parse the arguments
    args = parser.parse_args()

    # Check and create the weekly folder
    create_folder_if_not_exist(args.semester)
    create_folder_if_not_exist(f"./{args.semester.strip('/')}/{args.week.strip('/')}")
    create_folder_if_not_exist(f"./{args.semester.strip('/')}/{args.week.strip('/')}/notebook")
    create_file_if_not_exist(f"./{args.semester.strip('/')}/{args.week.strip('/')}/README.md")



import argparse
import os

readme_template = """
**Table of Content**
- [Lecture XX: The Title](#lecture-xx-the-title)
  - [Topics](#topics)
  - [Concepts](#concepts)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)

# Lecture XX: The Title

## Topics
Here are the topics we are going to cover
* [ ] TBD


## Concepts
* TBD


## Course materials
* slides [[link](TBD)]

# Suggested reading
* [If available] Chapter X of **Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter** (3rd Edition by Wes McKinney)
* Online resources
  * TBD
"""

notebook_template = """
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "(**You can also open this notebook in Google Colab**)\\n",
    "\\n",
    "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xiangshiyin/data-programming-with-python/blob/main/@semester@/@week@/notebook/code_demo.ipynb)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "data-programming-with-python-h2fMFruk-py3.10",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10.8"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
"""

def create_folder_if_not_exist(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        print(f"Folder {folder_path} already exists.")
    else:
        os.mkdir(folder_path)
        print(f"Folder {folder_path} created")

def create_file_if_not_exist(file_path, template=''):
    if os.path.exists(file_path) and os.path.isfile(file_path):
        print(f"File {file_path} already exists")
    else:
        with open(file_path, "w") as file:
            file.write(template)
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
    parser.add_argument("--notebook", action="store_true", help="generate jupyter notebook")

    # Parse the arguments
    args = parser.parse_args()

    # Check and create the weekly folder
    week_dir_path = f"./{args.semester.strip('/')}/{args.week.strip('/')}"
    notebook_dir_path = f"{week_dir_path}/notebook"
    data_dir_path = f"{week_dir_path}/data"
    pics_dir_path = f"{week_dir_path}/pics"
    readme_file_path = f"{week_dir_path}/README.md"
    notebook_file_path = f"{notebook_dir_path}/code_demo.ipynb"

    create_folder_if_not_exist(args.semester)
    create_folder_if_not_exist(week_dir_path)
    create_folder_if_not_exist(notebook_dir_path)
    create_folder_if_not_exist(data_dir_path)
    create_folder_if_not_exist(pics_dir_path)
    create_file_if_not_exist(
        file_path=readme_file_path,
        template=readme_template
    )
    if args.notebook:
        create_file_if_not_exist(
            file_path=notebook_file_path,
            template=notebook_template.replace(
                '@semester@', args.semester
            ).replace(
                '@week@', args.week
            )
        )



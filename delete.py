from pathlib import Path
import os
import shutil

## to see the branching mechanism 

def delete_files_with_os():
    os.remove('Golam/monster01.png')
    # os.remove('Golam/monster01.png')

def delete_files_with_pathlib():
    file = Path('Golam/monster02.png')
    file.unlink()

def delete_directory_os():
    os.rmdir('Rabby/')

def delete_directory_pathlib():
    directory = Path('screenshots/')
    directory.rmdir()

def delete_directory_including_subdirectory():
    shutil.rmtree('old-images/')

if __name__ == "__main__":
    delete_files_with_os()
    delete_files_with_pathlib()
    delete_directory_os()
    delete_directory_pathlib()
    delete_directory_including_subdirectory()
    



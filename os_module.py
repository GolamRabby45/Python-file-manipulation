import os


"""def display_cwd():
    cwd = os.getcwd()
    print("Current working directory:", cwd)"""



def display_directories(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                print("directory name:", entry.name)

"""
def display_files(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                print("File name: ", entry.name) """

if __name__ == "__main__":

    display_directories("11. Python for all/")
    #display_files("EE/")
    #display_cwd()
    

import os 


## to see the branching mechanism 

def top_down_walk():
    for dirpath, dirnames, files in os.walk('artwork/'):
        print("Directory:", dirpath)
        print("Include these directories")
        for dirname in dirnames:
            print(dirname)
        for file in files:
            print(file)
        print()


def bottom_up_walk():
    for dirpath, dirnames, files in os.walk('artwork/', topdown=False):
        print("Directory:", dirpath)
        print("Include these directories")
        for dirname in dirnames:
            print(dirname)
        for file in files:
            print(file)
        print()


if __name__ == "__main__":
    # top_down_walk()
    bottom_up_walk()


        
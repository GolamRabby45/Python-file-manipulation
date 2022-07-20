import os 

def make_logs_dir():
    try:
        os.mkdir('Golam/')
        os.mkdir('Rabby/')
        os.mkdir("GolamRabby/")
    except FileExistsError as e:
        print('Given named file already exists')

if __name__ == "__main__":

    make_logs_dir()

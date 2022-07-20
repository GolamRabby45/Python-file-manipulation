
def read_file():
    with open('./random_file.txt', 'r') as f:
        print(f.read(10))  # reads 10 bytes of data 
        f.close()

def read_file_readlines():
    with open('./random_file.txt', 'r') as f:
        lines = f.readlines()
        print(lines[1])
        f.close()



if __name__ == "__main__":
    #read_file()
    read_file_readlines()


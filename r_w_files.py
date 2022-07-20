
def read_file():
    with open('./random_file.txt', 'r') as f:
        contents = f.read()
        print(contents)
        f.close()

def write_file():
    with open('./random_file.txt', 'w') as f:
        f.write("I am Golam Rabby 1203045")
        f.close()

if __name__ == "__main__":
    write_file()
    read_file()




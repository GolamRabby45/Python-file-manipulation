
def print_content():
    f = open('./random_file.txt', 'r')
    contents = f.read()
    print(contents)
    f.close()

def write_new_content():
    f = open('./random_file.txt', 'w')
    f.write("I am Golam Rabby")
    f.close()



if __name__ == "__main__":
    # print_content()
    write_new_content()
    print_content()

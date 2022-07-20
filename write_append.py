
def write_content():
    with open('random_file.txt', 'w') as writer:
        for x in range(50): # 0 to 49 
            content = f'{x}\n'
            writer.write(content)

def append_content():
    with open('random_file.txt', 'a') as writer:
        for x in range(50, 100): # 50 to 99 
            content = f'{x}\n'
            writer.write(content)

if __name__ == "__main__":
    write_content()
    append_content()



import csv

def display_csv_reader():
    with open('monsters.csv') as f:
        reader = csv.reader(f, delimiter= ',')
        for row in reader:
            print(row[1])

def display_csv_reader_dict():
    with open('monsters.csv') as f:
        dictreader = csv.DictReader(f, delimiter= ',')
        for row in dictreader:
            print(row["monsterName"] + "is priced at " + row["price"])



if __name__ == "__main__":
    display_csv_reader()
    display_csv_reader_dict()



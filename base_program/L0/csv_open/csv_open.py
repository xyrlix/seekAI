import csv

def read_csv(file):
    with open(file, "r", encoding='utf-8') as f:
        csv_reader = csv.reader(f)

        headers = next(csv_reader)
        print("表头：", headers)

        for row in csv_reader:
            print(f"name: {row[0]}, age: {row[1]}, city: {row[2]}")


if __name__ == "__main__":
    read_csv("data.csv")
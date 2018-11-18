import csv

with open("dane/titanic_train.csv") as csvfile:
    data = csv.reader(csvfile,delimiter=",")
    for row in data:
        print(row)
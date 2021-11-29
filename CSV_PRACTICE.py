# https://www.youtube.com/watch?v=q5uM4VKywbA

import csv

# open the CSV - 'R' for read mode
with open('python_csv_practice.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
######################################################
######## HOW TO READ FROM A CSV ######################
# https://www.youtube.com/watch?v=q5uM4VKywbA
######################################################
import csv

# open the CSV - 'R' for read mode
with open('python_csv_practice.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
        
#####################################################################################        
# HOW TO WRITE TEXT TO A CSV
# Note that if you run multiple times, the file is appended each time
# because of the "a" permission in the open function.
# If the file is open in Windows you will get a Permission error when trying to run
######################################################################################
import csv
f = open("people.csv", "a", newline="")
tup1 = ("Patrick","Reed", 30)
writer = csv.writer(f)
writer.writerow(tup1)
tup2 = ("Patrick","Reed",25)
writer.writerow(tup2)
f.close()

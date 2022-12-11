import csv
with open("serialtest.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(",".join(row))

import csv

with open('jobtable.csv', 'r') as jobfile:
    with open('sortedpartitions.csv', 'r') as partfile:
       jobs = csv.reader(jobfile, delimiter=',', quotechar='"')
       parts = csv.reader(partfile, delimiter=',', quotechar='"')
       for part in parts:
           print(part)

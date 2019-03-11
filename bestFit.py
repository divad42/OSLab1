import csv
from manager import Manager

with open('jobtable.csv', 'r') as jobfile:
    with open('sortedpartitions.csv', 'r') as partfile:
        jobs = csv.reader(jobfile, delimiter=',', quotechar='"')
        parts = csv.reader(partfile, delimiter=',', quotechar='"')

        partitions = []

        for part in parts:
            partitions.append(part)
           
        man = Manager(partitions)

        for job in jobs:
            wait = 0
            while not (man.fitjob(job)):
                man.tick()
                wait += 1
            
            print("Fit job " + job[0] + " after " + str(wait) + " ticks.")

        print("done")


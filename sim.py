import csv
from manager import Manager

choose = int(input("1 for first fit, 2 for best fit: "))
if choose == 1:
    partitiontable = "unsortedpartitions.csv"
if choose == 2:
    partitiontable = "sortedpartitions.csv"

with open('jobtable.csv', 'r') as jobfile:
    with open(partitiontable, 'r') as partfile:
        jobs = csv.reader(jobfile, delimiter=',', quotechar='"')
        parts = csv.reader(partfile, delimiter=',', quotechar='"')

        partitions = []

        for part in parts:
            partitions.append(part)
           
        man = Manager(partitions)

        # Set up some metrics
        waits = []
        usage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for job in jobs:
            wait = 0
            while (not man.fitjob(job)):
                for i in range(len(man.parttable)):
                    if man.parttable[i][1] != -1:
                        usage[i] += 1
                man.tick()
                wait += 1 
            print("Wait time:", wait)
            waits.append(wait)
        print("DONE.")
        print("Metrics:")
        print("Average wait time:", sum(usage) / 10)
        for i in range(len(usage)):
            print("Partition", int(i+1), "in use for", int(usage[i]), "ticks.")
        print("Total fragmentation:", man.fragmentation)


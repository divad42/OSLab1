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
        queueLengths = []
        numjobs = 0
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
                queueLengths.append(int(job[0]) - 1) #first record the job numbers (the minus one will be helpful later)
            print("Wait time:", wait)
            waits.append(wait)
            numjobs += 1

        print("DONE.")
        print("Metrics:")
        print("Average wait time:", sum(waits) * 1.0 / len(waits))
        noUse = 0
        heavyUse = 0
        for i in range(len(usage)):
            print("Partition", int(i+1), "in use for", int(usage[i]), "ticks.")
            if usage[i] == 0:
                noUse += 1
            elif usage[i] >= 15:
                heavyUse += 1

        print("Percent of partitions never used:", 100 * round((noUse * 1.0) / len(usage), 3))
        print("Percent of partitions used heavily (at least 15 ticks):", 100 * round((heavyUse * 1.0) / len(usage), 3))

        print("Total fragmentation:", man.fragmentation)

        #now that we have the total number of jobs, we can find the length of the queue at each point recorded
        for i in range(len(queueLengths)):
            queueLengths[i] = numjobs - queueLengths[i]

        print("Average queue length per tick:", sum(queueLengths) * 1.0 / sum(waits))

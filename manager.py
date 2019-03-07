class Manager:
    """The actual class to perform the simulation. Each entry in the partition table is [size, job]. If the partition is not in use, job = -1. The job table is a dictionary storing [partition, timeRemaining]. Entries are deleted once the job completes."""
    parttable = []
    jobtable = {}
    def __init__(self, jobs, parts):
        self.jobs = jobs
        for part in parts:
            print(part)
            size = int(part[1])
            parttable.append([size, -1])


    def fitjob(self, job):
        for i in range(len(parttable)):
            if(parttable[i][1] == -1 and parttable[i][0] >= int(job[2])):
                jobtable[job[0]] = [i, job[1]]
                parttable[i][1] = job[0]
                return True

        return False

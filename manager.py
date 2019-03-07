class Manager:
    """The actual class to perform the simulation. Each entry in the partition table is [size, job]. If the partition is not in use, job = -1. The job table is a dictionary storing [partition, timeRemaining]. Entries are deleted once the job completes."""
    parttable = []
    jobtable = {}
    def __init__(self, parts):
        for part in parts:
            size = int(part[1])
            self.parttable.append([size, -1])

    def fitjob(self, job):
        if job[0] in self.jobtable.keys():
            raise ValueError("Job number " + str(job[0]) + " already exists.")
        for i in range(len(self.parttable)):
            if(self.parttable[i][1] == -1 and self.parttable[i][0] >= int(job[2])):
                self.jobtable[job[0]] = [i, job[1]]
                self.parttable[i][1] = job[0]
                return True

        return False

    def tick(self):
        deletion = []
        for key in self.jobtable.keys():
            job = self.jobtable[key]
            # Reduce time remaining
            job[1] -= 1
            if job[1] == 0: # Job is finished
                deletion.append(key)
        for key in deletion:
            job = self.jobtable[key]
            # Set the job's partition to be free and clear the entry from jobtable
            self.parttable[job[0]][1] = -1
            del self.jobtable[key]

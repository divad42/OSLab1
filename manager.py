class Manager:
    """The actual class to perform the simulation. Each entry in the partition table is [size, job]. If the partition is not in use, job = -1. The job table is a dictionary storing [partition, timeRemaining]. Entries are deleted once the job completes."""
    parttable = []
    jobtable = {}
    def __init__(self, jobs, parts):
        self.jobs = jobs
        for part in parts:
            size = int(part[1])
            this.parttable.append([size, -1])

    def tick(self):
        for key in self.jobtable.keys():
            job = self.jobtable[key]
            # Reduce time remaining
            job[1] -= 1
            if job[1] == 0: # Job is finished
                # Set the job's partition to be free and clear the entry from jobtable
                self.parttable[job[0]][1] = -1
                del self.jobtable[key]
                

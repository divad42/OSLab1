class Manager:
    """The actual class to perform the simulation. Each entry in the partition table is [size, job]. If the partition is not in use, job = -1. The job table is a dictionary storing [partition, timeRemaining]. Entries are deleted once the job completes."""
    parttable = []
    jobtable = {}
    fragmentation = 0

    def __init__(self, parts):
        for part in parts:
            size = int(part[1])
            self.parttable.append([size, -1])

    def fitjob(self, job):
        # Variables for R E A D A B I L I T Y
        jobnum = job[0]
        jobtime = int(job[1])
        jobsize = int(job[2])

        # Sanity check
        if jobnum in self.jobtable.keys():
            raise ValueError("Job number", jobnum, " already exists.")
        # Jobs larger than 9500 can't fit in any partition. No point wasting time on them.
        if jobsize > 9500:
            print("ERROR: Job", jobnum, "is too large to fit in any partition. Skipping.")
            return True
        for i in range(len(self.parttable)):
            size = self.parttable[i][0]
            usage = self.parttable[i][1]
            # If it's empty and can fit the partition, stick it in there
            if usage == -1 and size >= jobsize:
                # Create a job table entry and update the partition table entry
                self.jobtable[jobnum] = [i, jobtime]
                self.parttable[i][1] = jobnum
                print("Fit job", jobnum, "into partition", i, "with fragmentation:", size - jobsize)
                # Take fragmentation metric by adding leftover space
                self.fragmentation += size - jobsize
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

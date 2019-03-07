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

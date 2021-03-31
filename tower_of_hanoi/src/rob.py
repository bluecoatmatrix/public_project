class Rob:
    """
    Rob class to define Rob objects in Hanoi game. It contains a collection of Disks
    By default, the Disk collection is empty
    Operations:
        pushDisk: add disk to collection
        popDisk: remove and return the top disk from collection
        peekDisk: return the top disk
        getNumDisks: return total num of disks in collection
        getAllDisks: return all disks as a list in term of their <size>
    """
    def __init__(self, numOfDisks=0):
        self.disks = []

    def pushDisk(self, disk):
        self.disks.append(disk)

    def popDisk(self):
        if len(self.disks) == 0:
            raise Exception("This rob has nothing to pop!")
        return self.disks.pop()

    def peekDisk(self):
        if len(self.disks) == 0:
            raise Exception("This rob has nothing to peek!")
        return self.disks[len(self.disks)-1]

    def getNumDisks(self):
        return len(self.disks)

    def getAllDisks(self):
        disk_size = []
        for x in self.disks:
            disk_size.append(x.getSize())
        return disk_size

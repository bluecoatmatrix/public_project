from disk import Disk
from rob import Rob

class Hanoi:
    def __init__(self, numOfDisk=4):
        """
        Initialize game with 4 disks and 3 robs
        :param numOfDisk: default 4 disks
        """
        self.disk1 = Disk(1)
        self.disk2 = Disk(2)
        self.disk3 = Disk(3)
        self.disk4 = Disk(4)
        self.rob0 = Rob()
        self.rob1 = Rob()
        self.rob2 = Rob()
        self.rob0.pushDisk(self.disk4)
        self.rob0.pushDisk(self.disk3)
        self.rob0.pushDisk(self.disk2)
        self.rob0.pushDisk(self.disk1)
        self.robList = [self.rob0, self.rob1, self.rob2]

    def move(self, source, target):
        """
        Move the disk from source rob to target rob. Available rob index is from 0-2
        Rules to handle:
        1. source index is invalid: <0 or >2
        2. target index is invalid: <0 or >2
        3. source and target are the same
        4. source rob is empty
        5. source disk is bigger than top target disk

        :param source: index of rob moving from
        :param target: index of rob moving to
        """
        if source < 0 or source > 2:
            raise ValueError("Source index {} is invalid".format(source))
        if target < 0 or target > 2:
            raise ValueError("Target index {} is invalid".format(target))
        if source == target:
            raise ValueError("Source and Target index cannot be equal")
        if self.robList[source].getNumDisks() == 0:
            raise Exception("Source rob has nothing to move")

        source_disk = self.robList[source].peekDisk()
        if self.robList[target].getNumDisks()!=0:
            target_disk = self.robList[target].peekDisk()
            if source_disk.getSize() > target_disk.getSize():
                raise Exception("Invalid move, Source disk size is bigger than Target disk size!!!")
        self.robList[source].popDisk()
        self.robList[target].pushDisk(source_disk)

    def getState(self):
        """
        Get the complete state of current of 3 robs.
        :return: A json format for each rob listing of all disks on it in form of disk size
                 ie "rob0":[4,3,2]: it has 3 disks from bottom to top with size 4, 3, 2
        """

        s = '{'
        s += '"rob0": {}'.format(self.rob0.getAllDisks()) + ', '
        s += '"rob1": {}'.format(self.rob1.getAllDisks()) + ', '
        s += '"rob2": {}'.format(self.rob2.getAllDisks())
        s += '}'
        return s

    def isWin(self):
        """
        Checking if the tower of hanoi game is solved.
        :return: True if all 4 disks are on either rob1 or rob2; otherwise False
        """
        if(self.rob1.getNumDisks()==4 or self.rob2.getNumDisks() == 4):
            return True
        else:
            return False


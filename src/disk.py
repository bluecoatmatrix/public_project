class Disk:
    """Disk class to define disk objects in tower of hanoi
    """
    def __init__(self, size):
        self.size = size

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size
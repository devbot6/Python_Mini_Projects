
class student:
    def __init__(self, name, hours, apoints):
        self.name = name
        self.hours = float(hours)
        self.apoints = float(apoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getApoints(self):
        return self.apoints


class cellPhone:

    def __init__(self, manufact, model, price):
        self.newManufact = manufact
        self.newModel = model
        self.newPrice = price

    def setManufacturer(self, manufact):
        self.newManufact = manufact


    def setModel(self, model):
        self.newModel = model

    def setPrice(self, price):
        self.newPrice = price

    def getManufact(self):
        print(self.newManufact)

    def getModel(self):
        print(self.newManufact)

    def getPrice(self):
        print(self.newPrice)

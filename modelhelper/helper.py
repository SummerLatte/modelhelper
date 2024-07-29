import json
import matplotlib.pyplot as plt

class ModelHelper:
    def __init__(self, path, modelName) -> None:
            self.modelName = modelName
            self.path = path
            self.saveDict = {"trainLoss": [], "validLoss": [], "trainCorrect": [], "validCorrect": []}

    def saveDictJson(self):
        with open(f"{self.path}/{self.modelName}.json", "w+") as f:
            json.dump(self.saveDict, f)


    def loadSaveDict(self):
         with open(f"{self.path}/{self.modelName}.json", "r") as f:
            self.saveDict = json.load(f)

    def getMaxValidCorrect(self):
        return max(self.saveDict["validCorrect"])
    
    def getMinValidLoss(self):
        return min(self.saveDict["validLoss"])

    def saveLoss(self, train, valid):
        trainLoss = self.saveDict["trainLoss"]
        validLoss = self.saveDict["validLoss"]
        trainLoss.append(train)
        validLoss.append(valid)
        self.saveDictJson()

    def saveCorrect(self, train, valid):
        trainCorrect = self.saveDict["trainCorrect"]
        validCorrect = self.saveDict["validCorrect"]
        trainCorrect.append(train)
        validCorrect.append(valid)
        self.saveDictJson()

    def plotLoss(self):
        trainLoss = self.saveDict["trainLoss"]
        validLoss = self.saveDict["validLoss"]
        plt.plot(trainLoss, label="Train Loss")
        plt.plot(validLoss, label="Valid Loss")
        plt.legend()
        plt.show()

    def plotCorrect(self):
        trainCorrect = self.saveDict["trainCorrect"]
        validCorrect = self.saveDict["validCorrect"]
        plt.plot(trainCorrect, label="Train Correct")
        plt.plot(validCorrect, label="Valid Correct")
        plt.legend()
        plt.show()

# helper = ModelHelper("save", "model1")
# helper.saveLoss(1, 2)
# helper.saveLoss(2, 3)
# helper.saveCorrect(3, 4)
# helper.saveCorrect(4, 5)
# helper.plotLoss()
# helper.plotCorrect()
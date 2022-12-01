import random, os

class ShowInfo():
    def __init__(self,folder):
        self.folder = folder
        self.quotes = self.loadAsTextFile('quotes.txt')
        self.imageLocations = self.loadAsDirectory(folder + '/images/')
        self.facts = self.loadAsDict('facts.txt')

    def loadAsTextFile(self,fileName):
        f = open(self.folder + '/' + fileName, 'r', encoding='utf8')
        return f.readlines()

    def loadAsDirectory(self,folderName):
        return os.listdir(folderName)

    def loadAsDict(self,fileName):
        dict = {}
        f = open(self.folder + '/' + fileName, 'r', encoding='utf8') 
        allLines = f.readlines()
        for line in allLines:
#left of colon (keys), right of colon is (values)
            fields = line.split(':')  
            dict[fields[0].strip()] = fields[1].strip()
        return dict

    def getRandomQuote(self):
        return random.choice(self.quotes)

    def getRandomImage(self):
        return self.folder + "/images/" + random.choice(self.imageLocations).strip()

#=None makes this an optional parameter
    def getFact(self,factName=None): 
        if factName not in self.facts:
            return self.facts[random.choice(list(self.facts.keys()))]
#returns outside of the if statement (different indentantion)
        return self.facts[factName] 
# office_info = ShowInfo("office")


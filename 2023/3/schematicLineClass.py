import re

class NumberWithPosition:
    value=''
    position=[]

    def __init__(self, value, position):
        self.value = value
        self.position = position


class SchematicLine:
    id = 0
    line=""
    numbersWithPosition=[]

    def __init__(self, id=0, line=""):
        self.id = id
        self.line = line
        self.numberWithPosition = []

    def isSymbol(self, position):
        return len(re.findall("[\W\S_]", self.line[position])) > 0
    
    def isNumber(self, position):
        return len(re.findall("[0-9]", self.line[position])) > 0
    
    
    


class Vertex:
    def __init__(self, key) -> None:
        self.id = key
        self.connectedTo: dict = {}
        self.colour: str = 'white'
        self.distance: int = 0
        self.pred = None

    def setColour(self, colour):
        self.colour = colour
    
    def getColour(self):
        return self.colour
    
    def setDistance(self, distance):
        self.distance = distance
    
    def getDistance(self):
        return self.distance

    def setPred(self, pred):
        self.pred = pred
    
    def getPred(self):
        return self.pred
    
    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight
    
    def __str__(self) -> str:
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]


from Vertex import Vertex
from Graph import Graph
from Queue import Queue

def bfs(g: Graph, start: Vertex):
    list1: list = []
    start.setDistance(0)
    start.setPred(None)
    vertQueue: Queue[Vertex] = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert: Vertex = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColour() == 'white':
                nbr.setColour('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColour('black')
        list1.append(currentVert)
    return list1


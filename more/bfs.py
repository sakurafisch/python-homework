from Vertex import Vertex
from Graph import Graph
from Queue import Queue

def bfs(g: Graph, start: Vertex):
# def bfs(start: Vertex):
    list1: list = []
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColour() == 'white':
                nbr.setColour('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColour('black')
        list1.append(currentVert)
    return list1

def main() -> None:
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)
    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
    start = g.getVertex(0)

    list1 = bfs(g, start)
    # list1 = bfs(start)
    for i in list1:
        print(i)

if __name__ == '__main__':
    main()
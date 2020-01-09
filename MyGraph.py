class Graph:

    def __init__(self):

        self.amountOfNodes = 0
        self.adjacentDict = {}

    def addVertex(self, node):
        if node in self.adjacentList:
            print('node exists')
            return
        else:
            dict['key3'] = 'Geeks'
            self.adjacentDict[node] = []
            self.amountOfNodes += 1
    //
    def addEdge(self, node1, node2):

        #get node 1 existing values and append the new connection to node2
      
        #get node 2 existing values and append the new connection to node1

    def showConnections():


graph = Graph()
graph.addVertex('0')
graph.addVertex('1')
graph.addVertex('2')
graph.addVertex('3')
graph.addVertex('4')
graph.addVertex('5')
graph.addVertex('6')
graph.addEdge('3', '1')
graph.addEdge('3', '4')
graph.addEdge('4', '2')
graph.addEdge('4', '5')
graph.addEdge('1', '2')
graph.addEdge('1', '0')
graph.addEdge('0', '2')
graph.addEdge('6', '5')
graph.showConnections()
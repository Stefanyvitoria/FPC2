     
graph = Graph()
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")

graph.addEdge("A", "B")
graph.addEdge("C", "B")

graph.printGraph()

graph.deleteEdge("B", "A")

graph.printGraph() 
from grafo import Graph

graph = Graph()

graph.addNode("E1", []) #arad
graph.addNode("E2", []) #sibiu
graph.addNode("E3", []) #timissoara
graph.addNode("E4", []) #zerind
graph.addNode("E5", [])
graph.addNode("E6", [])
graph.addNode("E7", [])
graph.addNode("E8", [])
graph.addNode("E9", [])
graph.addNode("E10", [])
graph.addNode("E11", ['R'])
graph.addNode("E12", ['G'])
graph.addNode("E13", ['G', 'R'])
graph.addNode("E14", ['G'])

graph.addEdge("E1","E2")

graph.addEdge("E2","E3")
graph.addEdge("E2","E10")
graph.addEdge("E2","E9")

graph.addEdge("E3","E4")
graph.addEdge("E3","E13")
graph.addEdge("E3","E9")

graph.addEdge("E4","E5")
graph.addEdge("E4","E8")
graph.addEdge("E4","E13")

graph.addEdge("E5","E6")
graph.addEdge("E5","E7")
graph.addEdge("E5","E8")

graph.addEdge("E8","E9")
graph.addEdge("E8","E12")

graph.addEdge("E9","E11")

graph.addEdge("E13","E14")

# graph.printGraph() 

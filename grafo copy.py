class Node:
  def __init__(self, label, linha):
    self.label = label
    self.nodesAdj = {}
    self.linha = linha

  def __repr__ (self):
    return self.label
  
  def addNodeAdj(self, node, weight=None):
    self.nodesAdj[node.label] = weight
    return


class Graph:
  def __init__(self, nodes=[]):
      self.nodes = nodes
      self.linha_atual = None

  def getNode(self, label):
    for node in self.nodes:
      if node.label == label:
        return node
    return None

  def addNode(self, label, linha):
    self.nodes.append(Node(label=label, linha=linha))
    return
  
  def deleteNode(self, label):
    self.nodes = [node for node in self.nodes if node.label != label]
    return 

  def addEdge(self, label1, label2,weight=None):
    nodes = []
    for node in self.nodes:
      if node.label == label1 or node.label == label2:
        nodes.append(node)
        
    if len(nodes) > 2:
      raise Exception("Erro - labels repetidas!")   
    
    nodes[0].addNodeAdj(nodes[1],weight)
    nodes[1].addNodeAdj(nodes[0],weight)

  def deleteEdge(self, label1, label2):
    for node in self.nodes:
      if node.label == label1 or node.label == label2:
        for n in node.nodesAdj.keys():
          if n == label1 or n == label2:
            del node.nodesAdj[n]
            break 
              
    return

  def printGraph(self):
    [print((node.label,node.nodesAdj)) for node in self.nodes]
    return

  def adjNode(self, label):
    for node in self.nodes:
      if node.label == label:
        return node.nodesAdj 

       
graph = Graph()

graph.addNode("E1", ['B'])
graph.addNode("E2", ['B', 'Y'])
graph.addNode("E3", ['B', 'R'])
graph.addNode("E4", ['B', 'G'])
graph.addNode("E5", ['B', 'Y'])
graph.addNode("E6", ['B'])
graph.addNode("E7", ['Y'])
graph.addNode("E8", ['G', 'Y'])
graph.addNode("E9", ['R', 'Y'])
graph.addNode("E10", ['Y'])
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

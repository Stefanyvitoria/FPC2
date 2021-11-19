class Node:
  def __init__(self, label):
    self.label = label
    self.nodesAdj = []
  


class Graph:
  def __init__(self, nodes=[]):
      self.nodes = nodes

  def addNode(self, label):
    self.nodes.append(Node(label=label,))
    return
  
  def deleteNode(self):
    pass

  def addEdge(self):
    pass

  def deleteEdge(self):
    pass
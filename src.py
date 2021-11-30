def getTime(distancia, linhaatual, noDestino, hora_minuto):
  
  t1 = distancia

  linhas = {
    'G': 20,
    'B': 15,
    'Y': 7,
    'R': 10}

  if hora_minuto + linhas[linhaatual] > 1440:
    t2 = 240 + (1440 - hora_minuto)

  else:  
    t_espera = hora_minuto  - 240
    if (t_espera < 0) :
      t2 = abs(t_espera)
    elif (t_espera == 0):
      t2 = 0
    else:
      x = t_espera % linhas[linhaatual]
      t2 = 0
      if x != 0:
        t2 = linhas[linhaatual] - x

    if linhaatual not in noDestino.linha:
      if t2 < 4:
        t2 = linhas[linhaatual] - (4 - t2)

  return t1 + t2

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

distancia_heuristica = [
  [0.0, 15.0, 27.75, 37.2, 54.5, 58.1, 53.6, 38.1, 26.4, 13.6, 25.0, 40.9, 41.4, 44.7],
  [15.0, 0.0, 12.75, 22.2, 39.9, 43.6, 39.1, 25.9, 15.0, 5.25, 23.25, 31.3, 28.6, 32.7],
  [27.7, 12.75, 0.0, 9.45, 27.2, 30.9, 26.4, 20.4, 14.1, 15.4, 29.25, 28.6, 18.15, 25.2],
  [37.2, 22.2, 9.45, 0.0, 18.0, 21.5, 17.25, 18.6, 18.9, 25.0, 35.4, 27.9, 15.9, 23.1],
  [54.5, 39.9, 27.2, 18.0, 0.0, 4.5, 3.5, 29.0, 34.9, 42.3, 51.3, 37.2, 21.75, 26.8],
  [58.1, 43.6, 30.9, 21.5, 4.5, 0.0, 4.9, 33.45, 38.55, 45.45, 55.0, 41.4, 22.8, 27.2],
  [53.6, 39.1, 26.4, 17.25, 3.5, 4.9, 0.0, 30.0, 34.5, 40.95, 51.3, 38.55, 18.6, 23.4],
  [38.1, 25.9, 20.4, 18.6, 29.0, 33.4, 30.0, 0.0, 12.2, 30.4, 24.1, 9.6, 34.05, 41.4],
  [26.4, 15.0, 14.1, 18.9, 34.95, 38.55, 34.5, 12.2, 0.0, 20.25, 16.7, 16.35,31.8, 39.9],
  [13.6, 5.25, 15.4, 25.0, 42.3, 45.45, 40.95, 30.4, 20.25, 0.0, 26.4, 36.3, 28.0, 31.8],
  [25.0, 23.25, 29.25, 35.4, 51.3, 55.0, 51.3, 24.1, 16.7, 26.4, 0.0, 21.2, 47.25, 53.25],
  [40.95, 31.3, 28.6, 27.9, 37.2, 41.4, 38.55, 9.6, 16.35, 36.3, 21.2, 0.0, 43.1, 50.4],    
  [41.4, 28.6, 18.15, 15.9, 21.75 , 22.8, 18.6, 34.05, 31.8, 28.0, 47.25, 43.1, 0.0, 7.65],
  [44.7, 32.7, 24.9, 23.1, 26.8, 27.2, 23.4, 41.4, 39.9, 31.8, 53.2, 50.4, 7.65, 0.0]
]

distancia_real = [
  [0,15,0,0,0,0,0,0,0,0,0,0,0,0],
  [15,0,12.75,0,0,0,0,0,15,5.25,0,0,0,0],
  [0,12.75,0,9.45,0,0,0,0,14.1,0,0,0,28.05,0],
  [0,0,9.45,0,18.5,0,0,22.95,0,0,0,0,19.2,0],
  [0,0,0,18.5,0,4.5,3.6,45,0,0,0,0,0,0],
  [0,0,0,0,4.5,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,3.6,0,0,0,0,0,0,0,0,0],
  [0,0,0,22.95,45,0,0,0,14.4,0,0,9.6,0,0],
  [0,15,14.1,0,0,0,0,14.4,0,0,18.3,0,0,0],
  [0,0,5.25,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,18.3,0,0,0,0,0],
  [0,0,0,0,0,0,0,9.6,0,0,0,0,0,0],
  [0,0,28.05,19.2,0,0,0,0,0,0,0,0,0,7.65],
  [0,0,0,0,0,0,0,0,0,0,0,0,7.65,0]
]



def f_custo( no1, no2, hora, graph):
  minuto =  (hora[0]* 60) + hora[1]

  if graph.linha_atual == None:
    for l in no1.linha:
      if l in no2.linha:
        graph.linha_atual = l
  
  i= int(no1.label[1:])-1
  j = int(no2.label[1:])-1
  dr = distancia_real[i][j]
  h = getTime(dr, graph.linha_atual, no2, minuto)
  g = distancia_heuristica[int(no1.label[-1])-1][int(no2.label[-1])-1]
  return  h + g

def a_star_algorithm(no_start, no_end, hora_start, graph, heuristica):
  pass


print(f_custo(graph.getNode('E9'), graph.getNode("E11"), [22, 33], graph))
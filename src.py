from grafo import Graph, graph


def getTime(distancia, linhamantida, noOrigem, noDestino, hora_minuto):

  if noDestino.label == noOrigem.label:
    return 0

  t1 = distancia

  linhas = {
    'G': 20,
    'B': 15,
    'Y': 7,
    'R': 10}

  for l in noOrigem.linha:
      if l in noDestino.linha:
        linhaatual = l

  if hora_minuto + linhas[linhaatual] > 1440: #se começou antes das 04:00
    t2 = 240 + (1440 - hora_minuto)

  else:
    t_espera = hora_minuto  - 240
    if (t_espera < 0) : #chega antes as 04h
      t2 = abs(t_espera)
    elif (t_espera == 0): #chega exatamente as 04h
      t2 = 0
    else: #chega depois das 4h
      x = t_espera % linhas[linhaatual]
      t2 = 0
      if x != 0:
        t2 = linhas[linhaatual] - x

    if linhamantida not in noDestino.linha:
      if t2 < 4:
        t2 = linhas[linhaatual] - (4 - t2) + 4

  return t1 + t2


distancia_heuristica = [
  [0.0, 15.0, 27.75, 37.2, 54.5, 58.1, 53.6, 38.1, 26.4, 13.6, 25.0, 40.9, 41.4, 44.7], #1
  [15.0, 0.0, 12.75, 22.2, 39.9, 43.6, 39.1, 25.9, 15.0, 5.25, 23.25, 31.3, 28.6, 32.7], #2
  [27.7, 12.75, 0.0, 9.45, 27.2, 30.9, 26.4, 20.4, 14.1, 15.4, 29.25, 28.6, 18.15, 25.2], #3
  [37.2, 22.2, 9.45, 0.0, 18.0, 21.5, 17.25, 18.6, 18.9, 25.0, 35.4, 27.9, 15.9, 23.1], #4
  [54.5, 39.9, 27.2, 18.0, 0.0, 4.5, 3.5, 29.0, 34.9, 42.3, 51.3, 37.2, 21.75, 26.8], #5
  [58.1, 43.6, 30.9, 21.5, 4.5, 0.0, 4.9, 33.45, 38.55, 45.45, 55.0, 41.4, 22.8, 27.2], #6
  [53.6, 39.1, 26.4, 17.25, 3.5, 4.9, 0.0, 30.0, 34.5, 40.95, 51.3, 38.55, 18.6, 23.4], #7
  [38.1, 25.9, 20.4, 18.6, 29.0, 33.4, 30.0, 0.0, 12.2, 30.4, 24.1, 9.6, 34.05, 41.4], #8
  [26.4, 15.0, 14.1, 18.9, 34.95, 38.55, 34.5, 12.2, 0.0, 20.25, 16.7, 16.35,31.8, 39.9], #9
  [13.6, 5.25, 15.4, 25.0, 42.3, 45.45, 40.95, 30.4, 20.25, 0.0, 26.4, 36.3, 28.0, 31.8], #10
  [25.0, 23.25, 29.25, 35.4, 51.3, 55.0, 51.3, 24.1, 16.7, 26.4, 0.0, 21.2, 47.25, 53.25], #11
  [40.95, 31.3, 28.6, 27.9, 37.2, 41.4, 38.55, 9.6, 16.35, 36.3, 21.2, 0.0, 43.1, 50.4], #12
  [41.4, 28.6, 18.15, 15.9, 21.75 , 22.8, 18.6, 34.05, 31.8, 28.0, 47.25, 43.1, 0.0, 7.65], #13
  [44.7, 32.7, 24.9, 23.1, 26.8, 27.2, 23.4, 41.4, 39.9, 31.8, 53.2, 50.4, 7.65, 0.0] #14
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


def f_custo( no1_destino, no_destino_final, no2_origem, hora, graph):

  if graph.linha_atual == None:
    for l in no2_origem.linha:
      if l in no1_destino.linha:
        graph.linha_atual = l

  i= int(no1_destino.label[1:])-1
  j = int(no_destino_final.label[1:])-1
  h = distancia_heuristica[i][j]

  g = getTime(distancia_real[i][int(no2_origem.label[1:])-1], graph.linha_atual,  no2_origem, no1_destino, hora)
  return  (g, h + g)

def a_star_algorithm(no_start, no_end, hora_start, graph):
  caminho = [] #inicializa o caminho

  hora = hora_start[0]*60 + hora_start[1] #converte hr inicial para minutos
  fCusto = f_custo(no1_destino=no_start, no2_origem=no_start, no_destino_final=no_end, hora=hora_start, graph=graph) # calcula o tempo real e o temporeal + euristico
  no_start.pi='origem'
  fronteira = [[no_start, fCusto]]
  no_atual = None

  while len(fronteira) > 0:

    no_atual = min(fronteira, key=(lambda x: x[1][-1])) # pega o nó mais proximo do destino
    fronteira = [node for node in fronteira if node != no_atual]
    hora += no_atual[1][0] #adiciona horário atual do nó

    for node in graph.adjNode(no_atual[0].label):
      node = graph.getNode(node) #um no adj ao atual
      if node.pi == None: #verifica se o nó ja foi mapeado
        graph.setPi(node.label, no_atual[0])
        fCusto = f_custo(no2_origem=no_atual[0], no1_destino=node, no_destino_final=no_end, hora=hora, graph=graph)
        fronteira.append([node, fCusto]) #adiciona o nó na fronteira
      else:
        if no_atual[0].pi.label not in caminho: #verifica se o nó atual ja está no caminho
          caminho.append(no_atual[0].pi.label)

          if no_atual[0].label != no_start.label: 
            for l in graph.getNode(caminho[-1]).linha:
              if l in no_atual[0].linha:
                graph.linha_atual = l

        if node.label not in caminho: 
          fCusto = f_custo(no2_origem=no_atual[0], no1_destino=node, no_destino_final=no_end, hora=hora, graph=graph)
          fronteira.append([node, fCusto])

    if (no_atual[0].label == no_end.label): #verifica se o nó atual é o destino
      caminho.append(no_atual[0].label) #adiciona o nó no caminho
      break
  print("\nCaminho:")
  [print('->', e, end='') for e in caminho]


if __name__ == '__main__':
  print("Insira a Estação de Origem: \nEx (E1)")
  estacaoOrigem = input().upper()
  print("Insira a Estação de Destino: \nEx (E1)")
  estacaoDestino = input().upper()
  print("Insira a Hora de partida: \nEx (HH:MM)")
  hora,minuto = input().split(":")

  a_star_algorithm(graph.getNode(estacaoOrigem), graph.getNode(estacaoDestino), [int(hora),int(minuto)], graph )
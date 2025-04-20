import networkx as nx
from matplotlib import pyplot as plt
from Grafo import Grafo
from Djikstra import Djikstra
from FloydWarshall import FloydWarshall

# Declarando uma lista de adjacência que ajuda na criação da matriz de adjacência
lista_adj = [
    [[1, 4], [2, 6], [3, 13], [9, 4]],
    [[2, 2], [3, 9], [4, 10]],
    [[4, 7], [5, 2]],
    [[6, 2]],
    [[3, 1]],
    [[4, 5], [7, 1], [8, 3]],
    [[4, 1], [8, 1]],
    [[6, 3]],
    [[5, 2]],
    [[0, -3]]
]

print("Número total de vértices no grafo G: {}".format(len(lista_adj)))
print("\n")

G = Grafo()
G.criar_m_adj(lista_adj)
G.print_MatrizAdj()

g, pos = G.monta_grafo_networkx(738)
G.visualizar(g, pos)

# Teste

# Para Djikstra:

print("-" * 10 + "{:^20}".format("TESTANDO O ALGORITMO DE DJIKSTRA") + "-" * 10 + "\n")
djikstra = Djikstra(G)
djikstra.run(0)
djikstra.mostrar_caminho_minimo(8)
print("\n")

# Para Floyd-Warshall:

print("-" * 10 + "{:^20}".format("TESTANDO O ALGORITMO DE FLOYD-WARSHALL") + "-" * 10 + "\n")
fw = FloydWarshall()
fw.inicializaD(G)
fw.inicializaD_Pi()
fw.run()
fw.mostrar_caminho_minimo(0, 8)

# Colorindo o caminho mínimo

plt.figure(figsize=(8, 8), facecolor='#bde0fe')

# Desenhando o grafo:
print("-" * 43 + "{:^20}".format("DESENHANDO O GRAFO") + "-" * 43)

# Desenhando os vértices do grafo
nx.draw(g, pos, with_labels=True, node_color='#669bbc', node_size=500, edge_color='black', width=0.5)

caminho_min = [(0, 2), (2, 5), (5, 8)]

# Obtendo os pesos de cada aresta
pesos = {(u, v): d['weight'] for u, v, d in g.edges(data=True)}

# Destacando as arestas
nx.draw_networkx_edges(g, pos, edgelist=caminho_min, edge_color='orange', width=2)

# Desenhando as labels das arestas
nx.draw_networkx_edge_labels(g, pos, edge_labels=pesos, font_color='red')

# Mostrando o grafo
plt.title("Grafo da atividade")
plt.show()

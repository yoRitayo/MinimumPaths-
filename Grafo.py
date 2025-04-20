import numpy as np
import math
from prettytable import PrettyTable
import networkx as nx
import matplotlib.pyplot as plt


class Grafo:
    def __init__(self):
        self.m_adj = None
        self.l_adj = None
        self.nodes = []

    def print_MatrizAdj(self):
        """
        Mostrando a matriz de adjacência com Pretty Table.
        """

        labels = ["Vértice 0", "Vértice 1", "Vértice 2", "Vértice 3", "Vértice 4",
                  "Vértice 5", "Vértice 6", "Vértice 7", "Vértice 8", "Vértice 9"]

        tabela = PrettyTable()
        tabela.align = "c"
        tabela.header = True
        tabela.border = True
        tabela.padding_width = 2
        tabela.field_names = [" "] + labels

        # Iterando em cada linha da matriz de adjacência
        for id_vertice, linha in enumerate(self.m_adj):
            tabela.add_row([f"Vértice {id_vertice}"] + list(linha))

        print("-" * 68 + "{:^20}".format("MATRIZ DE ADJACÊNCIA") + "-" * 68)
        print(tabela)

    def criar_m_adj(self, l_adj):
        """
        Criando a matriz de adjacência a partir de uma lista de adjacência com indexação e convertendo o resultado
        final para o tipo np.array. Além disso, self.nodes é uma lista com os nós construída a partir do tamanho da
        lista de adjacência também.
        """
        self.m_adj = [[0 if i == j else math.inf for i in range(10)] for j in range(10)]

        for u, vizinhos in enumerate(l_adj):
            # Preenchendo self.nodes
            self.nodes.append(u)
            for v, peso in vizinhos:
                # Populando a matriz de adjacência
                self.m_adj[u][v] = peso

        self.m_adj = np.array(self.m_adj)
        self.l_adj = l_adj

    def monta_grafo_networkx(self, semente):
        """
        Gerando um grafo direcionado(DiGraph) para visualização e adicionando as arestas que se deseja desenhar.
        Além disso, se inicializa a semente para manter sempre o mesmo layout de grafo
        """

        g = nx.DiGraph()

        for u in range(10):
            for v in range(10):
                peso = self.m_adj[u][v]
                if not math.isinf(peso) and u != v:
                    g.add_edge(u, v, weight=peso)

        random_state = np.random.RandomState(semente)
        pos = nx.spring_layout(g, seed=random_state, k=1.5, scale=3)
        return g, pos

    def visualizar(self, g, pos):
        plt.figure(figsize=(9, 9), facecolor='#bde0fe')

        # Desenhando o grafo:
        print("-" * 43 + "{:^20}".format("DESENHANDO O GRAFO") + "-" * 43)

        # Desenhando os vértices do grafo
        nx.draw(g, pos, with_labels=True, node_color='#669bbc', node_size=500, edge_color='black', width=0.5)

        # Obtendo os pesos de cada aresta
        pesos = {(u, v): d['weight'] for u, v, d in g.edges(data=True)}

        # Desenhando as labels das arestas
        nx.draw_networkx_edge_labels(g, pos, edge_labels=pesos, font_color='red')

        # Mostrando o grafo
        plt.title("Grafo da atividade")
        plt.show()

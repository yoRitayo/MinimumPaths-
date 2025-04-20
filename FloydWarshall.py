import math
import copy


class FloydWarshall:
    """
    Algoritmo de Floyd-Warshall.
    """

    def __init__(self):
        self.D = None
        self.D_Pi = None

    def inicializaD(self, g):
        self.D = copy.deepcopy(g.m_adj)

    def inicializaD_Pi(self):
        # Inicializa D_pi vazia para manipulá-la
        n_nodes = len(self.D)

        self.D_Pi = [[None for _ in range(n_nodes)] for _ in range(n_nodes)]

        for u in range(n_nodes):
            for v in range(n_nodes):
                if u == v:
                    self.D_Pi[u][v] = '-'
                elif self.D[u][v] != math.inf:
                    self.D_Pi[u][v] = u
                else:
                    self.D_Pi[u][v] = '-'

    def run(self):
        n_nodes = len(self.D)
        for k in range(n_nodes):
            for u in range(n_nodes):
                for v in range(n_nodes):
                    if self.D[u][v] > self.D[u][k] + self.D[k][v]:
                        self.D[u][v] = self.D[u][k] + self.D[k][v]
                        self.D_Pi[u][v] = self.D_Pi[k][v]

        return self.D

    def mostrar_caminho_minimo(self, s, v):
        caminho = []
        atual = v

        if self.D_Pi[s][v] == '-':
            print("Não há caminho possível entre nós {} e {}.".format(s, v))
            return

        while atual != s:
            caminho.insert(0, atual)  # Dá um push front
            atual = self.D_Pi[s][atual]

            if atual == '-':
                print("Não há caminho possível entre nós {} e {}. ".format(s, v))
                return

        caminho.insert(0, s)

        print("Caminho mínimo:", caminho)
        print("Peso total do caminho encontrado", self.D[s][v])

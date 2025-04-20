import math
import heapq


class VertexDjikstra:
    def __init__(self, vertice):
        self.id = vertice
        self.d = math.inf
        self.pi = None


class Djikstra:
    """
    Algoritmo de Djikstra.
    """

    # Esse construtor é o Inicializa(G, s)
    def __init__(self, g):
        self.l_adj = g.l_adj
        self.nos = [VertexDjikstra(v) for v in g.nodes]

    def run(self, s):
        self.nos[s].d = 0
        heap = []

        # Adiciona o vértice VertexDjiktra(S) no heap
        heapq.heappush(heap, (self.nos[s].d, self.nos[s].id))

        visitados = set()

        while heap:
            u_d, u_id = heapq.heappop(heap)
            visitados.add(u_id)

            for v, peso in self.l_adj[u_id]:
                if v not in visitados and self.nos[v].d > u_d + peso:
                    self.nos[v].d = u_d + peso
                    self.nos[v].pi = u_id
                    heapq.heappush(heap, (self.nos[v].d, self.nos[v].id))

    def mostrar_caminho_minimo(self, v):
        if self.nos[v].d == math.inf:
            print(f"Não há caminho do vértice de origem até o vértice {v}.")
            return

        caminho = []
        atual = v

        # Enquanto um predecessor existir
        while atual is not None:
            caminho.insert(0, atual)
            atual = self.nos[atual].pi

        print("Caminho mínimo:", caminho)
        print("Peso total do caminho encontrado:", self.nos[v].d)

# Algoritmo de Djikstra

O algoritmo de Djikstra deve gerar um grafo tal qual:

```
G_pi = (V_pi, E_pi), onde:
V_pi = {v pertence ∈ V: v.pi ≠ nulo}
E_pi = {(v.pi, v) pertencente ∈ E}
```

Primeiramente, inicializa-se os vértices para execução do algoritmo.

```
Inicializa(G, s):
  para cada v ∈ G.V
  v.d = inf
  v.pi = nulo
  s.d = 0
```

A função acima será incorporada dentro da classe Djikstra criada para o algoritmo.

Após inicialização, é necessário relaxar os vértices para fazer a estimativa do custo local para alcançar um vértice.

```
Relaxa(u, v, w):
  se v.d > u.d + w(u, v)
  v.d = u.d + w(u, v)
  v.pi = u
```

```
Dijkstra(G, w, s):
  Inicializa(G, s)
  G = ∅
  Q = G.V
  visitados = {}

  enquanto Q ≠ ∅:
    u = extrair_min(Q)
    adiciona u ao conjunto de visitados
    
    para cada v ∈ G.Adj[u]
      se v ∉ visitados:
        Relaxa(u, v, w)
```

Onde Q é uma FP mínima, e extrar_min é definido como:

```
extrair_min(Q):
  minimo = Q.primeiro
  para cada v ∈ Q:
    faça se v.d < minimo.d
      então minimo = v
    retorna minimo
```

Este comportamento pode ser automatizado com ajuda de uma biblioteca como heapq.

Por fim, utiliza-se de G_pi gerado pelo Dijkstra, no qual a partir de um vértice qualquer v ∈ V:

```
mostrar_caminho_minimo(G_pi, v):
  caminho = []
  atual = v

  enquanto atual ≠ None:
    caminho.push_front(atual)
    atual = v.pi

  imprima("Caminho mínimo:", caminho)
```

# Pseudocódigo do algoritmo de Floyd-Warshall implementado

O algoritmo de FloydWarshall deve gerar uma matriz de adjacência d que armazenas os pesos das arestas de um grafo G tal qual:

```
InicializaD(G):
    para cada v ∈ G.V:
        d(v,v) = 0
    para cada (u, v) ∈ G.E:
        se (u,v) existe:
            d(u,v) = w(u,v)
        senão:
          d(u,v) = ∞
```

Essa inicialização é utilizada dentro da classe G. Portanto, dentro da classe FloydWarshall ela será apenas uma cópia da matriz de adjacência de G.

Além disso, deve se inicializar também a matriz de predecessores d.pi:

```
InicializaDPi(G):
  para cada u ∈ G.V:
    para cada v  ∈ G.V:
      d_pi(u, v) = u
      d_pi(u, u) = -(blank)
```

Executando o algoritmo:
```
FloydWarshall(d):
  para cada k ∈ d:
    para cada u ∈ d:
      para cada v ∈ d:
        se d(u,v) > d(u, k) + d(k,v):
          d(u,v) = d(u,k) + d(k, u)
          d_pi(u,v) = d_pi(u,k)
  
  retorna d
```

E para mostrar o caminho mínimo:

```
mostrar_caminho_mínimo(d_pi, s, v):
  caminho = []
  atual = v

  enquanto atual ≠ s:
    caminho.push_front(atual)
    atual = d_pi[s][atual]

  caminho.push_front(s)
  imprima("Caminho mínimo:", caminho)
```
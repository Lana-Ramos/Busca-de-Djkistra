import json
import heapq

def abrir_grafo(arquivo):
    try:
        with open(arquivo, "r") as f:
            grafo = json.load(f)
        return grafo
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
        return None
    except json.JSONDecodeError:
        print("Erro: Arquivo não está em formato JSON válido.")
        return None

def dijkstra(grafo, origem, destino):
    fila = [(0, origem)]
    distancias = {no: float("inf") for no in grafo}
    distancias[origem] = 0
    predecessores = {no: None for no in grafo}

    while fila:
        custo_atual, no_atual = heapq.heappop(fila)

        if no_atual == destino:
            break

        for vizinho, peso in grafo[no_atual].items():
            novo_custo = custo_atual + peso
            if novo_custo < distancias[vizinho]:
                distancias[vizinho] = novo_custo
                predecessores[vizinho] = no_atual
                heapq.heappush(fila, (novo_custo, vizinho))

    caminho = []
    no = destino
    while no is not None:
        caminho.insert(0, no)
        no = predecessores[no]

    return caminho, distancias[destino]

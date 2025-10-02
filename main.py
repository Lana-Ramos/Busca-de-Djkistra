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

if __name__ == "__main__":
    grafo = abrir_grafo("grafo.json")

    if grafo:
        try:
            origem = input("Digite o nó de origem: ").strip()
            destino = input("Digite o nó de destino: ").strip()

            if origem not in grafo or destino not in grafo:
                raise ValueError("Origem ou destino inválidos!")

            caminho, custo = dijkstra(grafo, origem, destino)
            if caminho:
                print(f"\nMelhor caminho: {' -> '.join(caminho)}")
                print(f"Custo total: {custo}")
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

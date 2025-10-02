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

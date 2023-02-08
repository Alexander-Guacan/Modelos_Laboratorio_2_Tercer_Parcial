from Grafo import Grafo

def main() -> None:
    # Generando grafo
    grafo = Grafo([[1], [2], [4], [0], [1, 5], [3, 0, 1]])
    # Ingresando nodo inicial y final a recorrer en el grafo
    nodo_inicial = int(input("Nodo inicial: "))
    nodo_objetivo = int(input("Nodo objetivo: "))
    # Imprimiendo todos los caminos posibles desde el nodo inicial hasta el nodo final
    print(f"Caminos posibles desde {nodo_inicial} hasta {nodo_objetivo}: ")
    print(grafo.caminos(nodo_inicial, nodo_objetivo))

if __name__ == "__main__":
    main()
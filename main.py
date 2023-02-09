from Grafo import Grafo

def imprimir_ubicaciones(ubicaciones: list[str]) -> None:
    i = 1
    # Imprimir cada ubicacion como un listado con su indice asociado
    for ubicacion in ubicaciones:
        print(f"{i}.- {ubicacion}")
        # Incrementar el indice de ubicacion
        i += 1

def main() -> None:
    # Ubicaciones por donde puede transitar la ambulancia
    ubicaciones = ["Ruminiahui", "La bota", "Quinta", "Hospital de Solca", "Llano chico", "La luz", "San Isidro del Inca", "Zambiza"]
    # Imprimir ubicaciones como menu
    imprimir_ubicaciones(ubicaciones)
    # Generando grafo
    grafo = Grafo([[5, 3, 1], [0], [3, 4], [], [2, 3, 7], [0], [3, 7], [4, 6]])
    # Ingresando nodo inicial y final a recorrer en el grafo
    nodo_inicial = int(input("Nodo inicial: "))
    nodo_objetivo = int(input("Nodo objetivo: "))

    # Contador de ruta
    i = 1
    # Imprimiendo todos los caminos posibles desde el nodo inicial hasta el nodo final
    print(f"Caminos posibles desde {nodo_inicial} hasta {nodo_objetivo}: ")
    for camino in grafo.caminos(nodo_inicial - 1, nodo_objetivo - 1):
        ruta = str()
        # Asociando el numero de cada nodo con el nombre de su ubicacion
        for nodo in camino:
            # Formato de impresion
            ruta += ubicaciones[nodo] + (" -> " if nodo != camino[-1] else "")
        # Impresion de cada ruta
        print(f"{i}.- {ruta}")
        # Impresion de costo por ruta
        print(f"[Costo = {len(camino)}]")
        i += 1
        
if __name__ == "__main__":
    main()
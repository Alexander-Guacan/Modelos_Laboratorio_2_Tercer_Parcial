class Grafo:
    """
    Estructura de datos que representa un grafo a traves del uso de lista de listas, donde cada lista representa un nodo y cada elemento de cada lista representa el numero del nodo del o los hijos que apunta cada uno

    Atributos:
        nodos

    Metodos:
        __caminos_recursivo
        caminos
    """
    def __init__(self, nodos: list[list[int]]) -> None:
        """
        Constructor donde se especifica el orden y estructura del grafo

        Args:
            nodos (list[list[int]]): _description_ Capa posicion en la lista de listas es cada grafo, y cada sublista es es sus hijos
        """
        self.__nodos = nodos

    def __caminos_recursivo(self, nodo_actual: int, nodo_objetivo: int, caminos: list[list[int]], camino = 0) -> tuple[list[list[int]], int]:
        """
        Retorna todos los caminos posibles desde un punto o nodo inicial hasta el nodo objetivo o hasta que llegue a un nodo hoja

        Args:
            nodo_actual (int): _description_ Nodo en el que se encuentra en el grafo
            nodo_objetivo (int): _description_ Nodo final al que se desea llegar
            caminos (list[list[int]]): _description_ Lista de caminos posibles
            camino (int, optional): _description_. Defaults to 0. Numero de camino posible, sirve como indice para la lista de caminos

        Returns:
            tuple[list[list[int]], int]: _description_ Retorna los caminos y el numero de caminos
        """

        if len(caminos[camino]) > 0 and nodo_actual == caminos[camino][0]:
            return caminos, camino + 1

        # Agregamos el nodo que estamos accediendo al recorrido
        caminos[camino].append(nodo_actual)

        # Si el nodo a recorrer es el nodo objetivo
        if nodo_actual == nodo_objetivo:
            return caminos, camino + 1
        
        # Si el nodo tiene uno o mas de un hijo
        for hijo in self.__nodos[nodo_actual]:
            camino = self.__caminos_recursivo(hijo, nodo_objetivo, caminos, camino)[1]
            
            # Es el ultimo hijo del nodo
            if hijo == self.__nodos[nodo_actual][-1]:
                return caminos, camino

            # Creando un nuevo camino
            caminos.append([])
            
            # Itera la rama padre
            i = 0
            # Punto de quiebre con el nodo padre del nodo actual
            nodo = -1

            # Copiando la rama padre
            while nodo != nodo_actual:
                # Agregando al nuevo camino los nodos recorridos anteriores a esta nueva ramificacion
                caminos[camino].append(caminos[camino - 1][i])
                # Avanzamos al siguiente nodo en la lista recorrida
                nodo = caminos[camino - 1][i]
                # Incrementamos la posicion de la lista de nodos recorridos
                i += 1

        return caminos, camino + 1

    def caminos(self, nodo_inicial: int, nodo_final: int) -> list[list[int]]:
        """
        Retorna todos los caminos posibles desde un nodo inicial hasta un nodo final

        Args:
            nodo_inicial (int): _description_ Nodo o punto inicial desde donde se generaran los caminos
            nodo_final (int): _description_ Nodo o punto final hasta donde debe recorrerse el camino

        Returns:
            list[list[int]]: _description_ Caminos posibles desde el nodo inicial hasta el nodo final
        """
        # Calculamos todos los caminos por los que se puede mover en el grafo desde el nodo inicial hasta los nodos hoja
        # La funcion retorna la lista de caminos y el numero de caminos, usamos [0] para obtener solo la lista de caminos
        caminos_encontrados = self.__caminos_recursivo(nodo_inicial, nodo_final, [[]])[0]
        
        # Listado de caminos que llegan al nodo final
        caminos_validos = list[list[int]]()
        # Obtenemos cada camino posible del grafo
        for camino in caminos_encontrados:
            # Un camino es valido si su valor final es el nodo final especificado por parametro
            if len(camino) >= 0 and camino[-1] == nodo_final:
                # Agregamos el camino que llega al nodo final
                caminos_validos.append(camino)
    
        return caminos_validos
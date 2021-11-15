class Edge:
    def __init__(self, x, y, weight):
        """Instancia uma nova aresta, onde 'x' e 'y' são os índices dos vértices aos quais ela se conecta e 'weight' é o peso."""
        self.vertices = [x, y]
        self.weight = weight

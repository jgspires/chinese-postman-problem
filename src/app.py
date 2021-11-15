from entities.Graph import Graph


def main():
    graphs = []

    # Grafo 1:
    g1 = Graph(6)
    g1.add_edge(0, 1, 1)
    g1.add_edge(0, 2, 2)
    g1.add_edge(1, 3, 3)
    g1.add_edge(1, 5, 7)
    g1.add_edge(2, 3, 5)
    g1.add_edge(2, 5, 4)
    g1.add_edge(3, 4, 6)
    g1.add_edge(4, 5, 8)
    graphs.append(g1)

    # Grafo 2
    g2 = Graph(5)
    g2.add_edge(0, 1, 1)
    g2.add_edge(0, 2, 4)
    g2.add_edge(0, 3, 4)
    g2.add_edge(1, 2, 2)
    g2.add_edge(1, 3, 2)
    g2.add_edge(1, 4, 3)
    g2.add_edge(2, 3, 5)
    g2.add_edge(3, 4, 6)
    graphs.append(g2)

    # Grafo 3
    g3 = Graph(5)
    g3.add_edge(0, 1, 1)
    g3.add_edge(0, 2, 3)
    g3.add_edge(1, 2, 5)
    g3.add_edge(1, 3, 2)
    g3.add_edge(1, 4, 4)
    g3.add_edge(2, 3, 9)
    g3.add_edge(3, 4, 4)
    graphs.append(g3)

    print("\nProblema do Carteiro Chinês | Problema da Inspeção de Rotas:\n")
    for i, graph in enumerate(graphs):
        print(f"Grafo {i+1}:\n")
        print(
            f"   Arestas Eulerizadas: {graph.get_shortest_path_distance()['combination']}\n"
        )
        for j in range(graph.v_num):
            postman = graph.chinese_postman(j)
            print(f"   Caminho Partindo de {j}: {postman['path']}")
        print(f"\n   Distância: {postman['distance']}")
        print("\n------------------------------\n")


if __name__ == "__main__":
    main()

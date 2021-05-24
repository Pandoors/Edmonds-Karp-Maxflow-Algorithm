from edmonds_karp import MaxFlowFinder
from graph_definition.edge import Edge
from graph_definition.vertex import Vertex
from graph_definition.digraph import Digraph

if __name__ == "__main__":
    test_graph = Digraph()
    test_graph.get_from_file('adjacency_lists/graph1.json')
    test_graph.draw("graph1.png")
    v1 = Vertex(0)
    v2 = Vertex(6)
    alg = MaxFlowFinder(test_graph)
    alg.edmondsKarpAlgorithm(v1, v2)

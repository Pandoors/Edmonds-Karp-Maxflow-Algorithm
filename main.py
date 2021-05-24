from edmonds_karp import MaxFlowFinder
from graph_definition.vertex import Vertex
from graph_definition.digraph import Digraph

if __name__ == "__main__":
    test_graph = Digraph()
    test_graph.get_from_file('adjacency_lists/graph3.json')
    test_graph.draw("graph3.png")
    v1 = Vertex(0)
    v2 = Vertex(10)
    alg = MaxFlowFinder(test_graph)
    print("Result maximum flow: "+str(alg.edmondsKarpAlgorithm(v1, v2)))
    test_graph.draw("graph3_residual.png")



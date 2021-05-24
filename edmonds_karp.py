from graph_definition.edge import Edge
from graph_definition.vertex import Vertex
from graph_definition.digraph import Digraph


class MaxFlowFinder:
    """
        The "brain" of whole project. Class made for finding the maximum flow of the graph with
        Edmonds Karp algorithm implementation. The BFS path finder has been defined in graph class.
        Attributes
        ----------
        graph : already created and "contested" graph that the solver wants to perform on

        Methods
        ----------
        edmondsKarpAlgorithm: Edmonds Karp implementation of Ford Fulkerson's graph's max flow finder method.
        src, dest are the starting and ending point of the algorithm. Performs a search for the max flow and returns
        the max flow (int). Also prints important information such as all the paths.
    """

    def __init__(self, graph: Digraph):
        self.graph = graph

    def edmondsKarpAlgorithm(self, src, dest):
        flow = 0
        src.clear_visit()
        dest.clear_visit()
        path = self.graph.get_shortest_path(src, dest)

        while path is not None:
            _s = ""
            for x in path:
                _s += str(x) + "->"
            _s = _s[0:len(_s) - 2]
            print("\nprinting path: " + _s)
            edgesInPath = []
            for vert_idx in range(0, len(path) - 1):
                edge = self.graph.get_edge_from_vertices(path[vert_idx], path[vert_idx + 1])
                edgesInPath.append(edge)
            min_flow = min([edge.flowAvailable for edge in edgesInPath])
            for edge in edgesInPath:
                self.graph.lowerFlowGivenEdge(edge, min_flow)
                if self.graph.hasEdgeFlipped(edge.src, edge.dest, min_flow):
                    pass
                else:
                    self.graph.createEdgeFlipped(edge.dest, edge.src, min_flow)

            flow += min_flow
            print("actual minimum flow of edges: " + str(min_flow))
            print("actual maximum flow of graph: " + str(flow))
            if flow != 4:
                path = self.graph.get_shortest_path(src, dest)
            else:
                path = self.graph.get_shortest_path(src, dest)
            print(self.graph)
            # print("flow summary: " + str(flow))

        return flow

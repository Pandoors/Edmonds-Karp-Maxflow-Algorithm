from graph_definition.edge import Edge
from graph_definition.vertex import Vertex
from graph_definition.digraph import Digraph


class MaxFlowFinder:
    def __init__(self, graph: Digraph):
        self.graph = graph

    def edmondsKarpAlgorithm(self, src, dest):
        flow = 0
        src.clear_visit()
        dest.clear_visit()
        path = self.graph.get_shortest_path(src, dest)

        while path is not None:
            print("printing path: \n")
            _s = ""
            for x in path:
                _s += str(x) + "->"
            print(_s)
            edgesInPath = []
            for vert_idx in range(0, len(path) - 1):
                edge = self.graph.get_edge_from_vertices(path[vert_idx], path[vert_idx + 1])
                edgesInPath.append(edge)
            min_flow = min([edge.flowAvailable for edge in edgesInPath])
            for edge in edgesInPath:
                self.graph.lowerFlowGivenEdge(edge, min_flow)
            flow += min_flow
            print("minimum flow: " + str(min_flow))
            path = self.graph.get_shortest_path(src, dest)
            print(self.graph)
            print("\n")
            print("flow summary: " + str(flow))

        return flow

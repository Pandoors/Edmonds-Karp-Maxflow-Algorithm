from graph_definition.vertex import Vertex


class PlainEdge:
    """
    Class representing edge without weight without direction
    Attributes
    ----------
    nodes : connected vertices
    """
    nodes = []

    def __init__(self, first_vertex: Vertex, second_vertex: Vertex):
        self.nodes.append(first_vertex)
        self.nodes.append(second_vertex)

    def get_nodes(self):
        return self.nodes


class Edge(PlainEdge):
    """
    Class representing weighted edge from directed graph. Has attributes
    needed to Edmond Karp algorithm
    inherits from plain edge
    Attributes
    ----------
    src : starting vertex of edge
    dest : ending vertex of edge
    weight : weight of edge.
    flow : maximum flow of edge needed to Edmonds Karp algorithm
    flowAvailable :  attribute needed to Edmonds Karp algorithm
    """

    def __init__(self, src: Vertex, dest: Vertex, weight: int):
        super().__init__(src, dest)
        self.src = src
        self.dest = dest
        self.weight = weight
        self.flowAvailable = self.weight
        self.flow = self.weight

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def get_weight(self):
        return self.weight

    def getAvailableFlow(self):
        return self.flowAvailable

    def getFlow(self):
        return self.flow

    def lowerFlow(self, to_lower):
        self.flowAvailable -= to_lower

    def clearActualFlow(self):
        self.flowAvailable = self.flow

    def __str__(self):
        if self.flow > 0:
            return '( ' + str(self.src.get_name()) + ' --> ' + \
                   str(self.dest.get_name()) + ' ) with weigh: ' \
                   + str(self.get_weight()) + ' with flow: ' + str(self.getFlow()) \
                   + ' with remaining flow: ' + str(self.getAvailableFlow())
        else:
            return '( ' + str(self.src.get_name()) + ' --> ' + \
                   str(self.dest.get_name())  \
                   + ' ) residual edge with remaining flow: ' + str(self.getAvailableFlow())

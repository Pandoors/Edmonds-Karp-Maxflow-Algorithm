from graph_definition.edge import Edge
from graph_definition.vertex import Vertex
import abc
import json
from networkx.drawing.nx_agraph import to_agraph
import networkx as nx
import queue


class Graph(metaclass=abc.ABCMeta):
    """
    Abstract Graph class

    Attributes
    ----------
    vertices : single vertices existing in graph
    edges : dictionary where key is starting point of edge,
    values are ending points of edge
    edgeList : list of all edges in graph
    """

    def __init__(self):
        self.vertices = []
        self.edges = {}
        self.edgeList = []

    @abc.abstractmethod
    def add_vertex(self, vertex: Vertex):
        pass

    @abc.abstractmethod
    def add_edge(self, edge: Edge):
        pass


class Digraph(Graph):
    """
        Class representing directed graph with weights.
        Has methods and Attributes necessary to Edmonds Karp algorithm

        Methods
        ----------
        add_vertex: adds vertex to self.vertices and creates a key in self.edges
        add_edge: creates a pointing edge and adds it to self.edgeList. Dict Key=vertex.name -> Value=[vertex]
        Also adds it to a dictionary self.edges
        coming_out_of: returns all vertices coming out of vertex given
        has_vertex: boolean method to determine if a vertex exists
        get_from_file: reads json (adjacency list) and maps it into digraph class
        json format is [ [ [name of vertex, weight], [name of vertex, weight], ...], ...]
        get_vertices_names: returns a list of names of vertices
        draw: takes a name of file (eg "example.png"), creates a graph drawing and stores
        it in "networkx_files/". Note that it only creates the vertices and edges pointing
        in right directions. It is just for the visualisation of graph. The weights/flow of vertices are not shown.
        get_shortest_path: breadthFirstSearch usage to find the shortest path in graph
        clear_visits_bfs: marks all vertices not visited
        hasEdgeFlipped: return True if residual (fake) edge of given edge has been created in graph and also adds the
        flow to this edge
        createEdgeFlipped: if residual edge does not exists - it creates one and assigns the flow to that edge
        get_edge_from_vertices: returns an edge (residual or forward) of the given Vertices
        clear_visits_bfs: resets the "visited" attribute of Edge for the sake of BFS find path method
        lowerFlowGivenEdge: lowers the flow of given edge



    """

    def __init__(self):
        super().__init__()

    def add_vertex(self, vertex: Vertex):
        names = self.get_vertices_names()
        if vertex.name not in names:
            self.vertices.append(vertex)
            self.edges[vertex.name] = []

    def add_edge(self, edge: Edge):
        start = edge.get_source()
        end = edge.get_destination()
        names = self.get_vertices_names()
        if not (start.name in names and end.name in names):
            raise ValueError('one of vertices or both are not in graph')
        self.edges[start.name].append(end)
        self.edgeList.append(edge)

    def hasEdgeFlipped(self, start: Vertex, end: Vertex, min_flow: int):
        for edge in self.edgeList:
            if edge.src == end and edge.dest == start:
                edge.flowAvailable += min_flow
                return True
        return False

    def createEdgeFlipped(self, start: Vertex, end: Vertex, min_flow: int):
        edgeFlipped = Edge(start, end, 0)
        edgeFlipped.flowAvailable = min_flow
        self.edgeList.append(edgeFlipped)
        self.edges[start.name].append(end)

    def get_edge_from_vertices(self, start: Vertex, end: Vertex) -> Edge:
        for edge in self.edgeList:
            if edge.src.name == start.name and edge.dest.name == end.name:
                return edge

        # although it will never happen
        raise ValueError('there is no edges from given input')

    def coming_out_of(self, vertex):
        return self.edges[vertex.name]

    def has_vertex(self, vertex):
        return vertex in self.vertices

    def clear_visits_bfs(self):
        [vert.clear_visit() for vert in self.vertices]

    def get_from_file(self, source):
        with open(source) as json_file:
            data = json.load(json_file)
        print("Got json: " + str(data))

        for vert in range(0, len(data)):
            vertex = Vertex(vert)
            self.add_vertex(vertex)
            for vert_in in range(0, len(data[vert])):
                vertex_in = Vertex(data[vert][vert_in][0])
                self.add_vertex(vertex_in)
                edge = Edge(vertex, vertex_in, data[vert][vert_in][1])
                self.add_edge(edge)

    def get_vertices_names(self) -> list:
        return [ver.name for ver in self.vertices]

    def lowerFlowGivenEdge(self, e: Edge, minFlow: int):
        for edge_idx in range(0, len(self.edgeList)):
            if self.edgeList[edge_idx].src == e.src and self.edgeList[edge_idx].dest == e.dest:
                self.edgeList[edge_idx].lowerFlow(minFlow)
                """Helpful print()"""
                # print("printing lowered edge: src: " + str(self.edgeList[edge_idx].src.name) + " dest: " + str(
                #     self.edgeList[edge_idx].dest.name) + " flow: " + str(
                #     self.edgeList[edge_idx].flow) + " availableFlow: " + str(
                #     self.edgeList[edge_idx].flowAvailable) + " lowered by: " + str(minFlow))

    def draw(self, path):
        g = nx.DiGraph()
        for edge in self.edgeList:
            g.add_edge(edge.src.name, edge.dest.name, weight=edge.weight)
        output_path = "networkx_files/" + path
        agraph = to_agraph(g)
        agraph.layout('dot')
        agraph.draw(output_path)

    def get_shortest_path(self, start: Vertex, end: Vertex):
        self.clear_visits_bfs()
        start.clear_visit()
        end.clear_visit()
        visited = set()
        q = queue.Queue()
        q.put([start])

        while not q.empty():
            path = q.get()

            vertex = path[-1]
            if vertex.name == end.name:
                return path
            elif vertex not in visited:
                for child in self.coming_out_of(vertex):
                    if self.get_edge_from_vertices(vertex, child).flowAvailable > 0:
                        path_ = list(path)
                        path_.append(child)
                        q.put(path_)

                visited.add(vertex)

    def __str__(self):
        output = "Graph edges: \n"
        for edge in self.edgeList:
            output = output + str(edge) + "\n"
        return output

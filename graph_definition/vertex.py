class Vertex:
    """
    Class representing vertex/node in graph
    Attributes
    ----------
    name : int name of vetex
    visited : bool for BFS purpose
    """

    def __init__(self, name: int):
        self.name = name
        self.visited = False

    def get_name(self):
        return self.name

    def is_visited(self):
        return self.visited

    def mark_visited(self):
        self.visited = True

    def clear_visit(self):
        self.visited = False

    def __str__(self):
        return '( ' + str(self.name) + ' )'

    # def __eq__(self, other):
    #     if not isinstance(other, Vertex):
    #         # don't attempt to compare against unrelated types
    #         return NotImplemented
    #
    #     return self.name == other.name and self.visited == other.visited

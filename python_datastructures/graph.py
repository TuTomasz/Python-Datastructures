"""In computer science, a graph is an abstract data type that is meant to implement the undirected graph and directed graph concepts from the field of graph theory within mathematics."""


class Vertex:
    def __init__(self, value):
        self.value = value
        self.next = None


class Graph:
    def __init__(self, type=None):
        self.edges = {}


if __name__ == "__main__":
    pass

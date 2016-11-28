

class UndirectedGraph(object):

    def __init__(self, list_of_tuples):
        self.graph = {}
        assert isinstance(list_of_tuples, list)
        for tup in list_of_tuples:
            assert isinstance(tup, tuple)
            assert len(tup) == 2

            if tup[0] not in self.graph:
                self.graph[tup[0]] = set()
            if tup[1] not in self.graph:
                self.graph[tup[1]] = set()

            self.graph[tup[0]].add(tup[1])
            self.graph[tup[1]].add(tup[0])

class UndirectedEdge(object):
    weight = -1
    node1 = None
    node2 = None

class UndirectedWeightedGraph:
    def __init__(self, list_of_tuples):


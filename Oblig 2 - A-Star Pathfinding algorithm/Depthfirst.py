class Vertex():

    def __init__(self, name, adjecencyList=[]):
        self.name = name
        self.adjecent = adjecencyList
        self.distance = None
        self.previous = None
        self.known = False


class Edge():

    def __init__(self, weight, vertex):
        self.vertex = vertex
        self.weight = weight


class Graph():

    def __init__(self):
        self.vertecies = {}

    def dfs(self, graph, node):
        if startVertexName not in self.vertecies:
            raise KeyError('Error')
        for v in self.vertecies:
            vertex = self.vertecies[v]
            vertex.distance = None

        from queue import SimpleQueue
        queue = SimpleQueue()

        def enqueue(data):
            queue.put(data)

        def dequeue():
            return queue.get()

        self.vertecies[startVertexName].distance = distance = 0

        enqueue(self.vertecies[startVertexName])

        while not queue.empty():
            eyeball = dequeue()
            if eyeball.distance is None:
                eyeball.distance = distance
            for edge in eyeball.adjecent:
                if edge.vertex.distance is None:
                    edge.vertex.distance = eyeball.distance +1
                    enqueue(edge.vertex)
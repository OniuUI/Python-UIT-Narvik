from Vertex import Vertex
from Edge import Edge

class Graph():
    
    def __init__(self):
        self.__vertecies = {}

    @property
    def vertecies(self):
        return self.__vertecies
        
    def addEdge(self, from_v = None, to_v = None, weight = 1):
        if from_v and to_v:
            if from_v not in self.__vertecies:
                self.__vertecies[from_v] = Vertex(name = from_v)
            if to_v not in self.__vertecies:
                self.__vertecies[to_v] = Vertex(name = to_v)
            edge = Edge(weight, self.__vertecies[to_v])
            
            self.__vertecies[from_v].add_adjecent_edge(edge)
        else:
            raise Exception("Illegal edge definition")

    def __str__(self):
        retval = ''
        for v in self.vertecies:
            vertex = self.vertecies[v]
            retval += v + '(' + str(vertex.distance) + ')'
            for e in vertex.adjecent:
                retval += ' --> [' + e.vertex.name + ': ' + str(e.weight) + ']: ' + str(e.vertex.distance)
            retval += '\n'
        return retval            
    
    def readFile(self, filename = None):
        import pandas as pd
        from collections import namedtuple
        
        columnnames = ['vertex_from', 'vertex_to', 'weight']
        df = pd.read_csv(filename, error_bad_lines=False, 
                         encoding='latin-1', warn_bad_lines=False, 
                         names=columnnames, header = None, sep = ';')
        edge = namedtuple('edge', ['vertex_from','vertex_to','weight'])
        def maketuple(vertex_from ='', vertex_to ='', weight = 0):
            return edge(vertex_from = vertex_from, 
                        vertex_to = vertex_to, 
                        weight = weight)
        # Convert pandas representation into namedtuples
        edges = [maketuple(vertex_from, vertex_to, weight) 
                 for vertex_from, vertex_to, weight 
                 in zip(df['vertex_from'], df['vertex_to'], df['weight'])]
        for e in edges:
            self.addEdge(e.vertex_from, e.vertex_to, e.weight)
    
    def unweightedPathDistance(self, startVertexName):
        self.resetGraph()
        # Give an exception if startnode does not exist
        if startVertexName not in self.vertecies:
            raise KeyError("Startnode not present in graph")
        # ... and initialize
        for v in self.vertecies:
            vertex = self.vertecies[v]
            vertex.distance = None
            
        # Create a FIFO-queue and define enqueue / dequeue
        from queue import SimpleQueue       
        queue = SimpleQueue()  

        def enqueue(data):
            queue.put(data)
        def dequeue():
            return queue.get()
        
        self.vertecies[startVertexName].distance = distance = 0
        enqueue(self.vertecies[startVertexName])
        
        previous_node = None
        while not queue.empty():
            eyeball = dequeue()
            # print("Visiting .... " + eyeball.name)
            if eyeball.distance is None:
                eyeball.distance = distance
                eyeball.previous = previous_node
            for edge in eyeball.adjecent:
                if edge.vertex.distance is None:
                    edge.vertex.distance = eyeball.distance + 1
                    edge.vertex.previous = eyeball
                    enqueue(edge.vertex)
            previous_node = eyeball
        
    def getPath(self, fromVertex, toVertex):
        # To verify if a path exists, the path has to be updated ...
        #self.unweightedPathDistance(fromVertex)
        # Need to verify that the destination vertex exists within the graph
        if toVertex not in self.vertecies:
            raise KeyError("Destination node not present in graph")
        from queue import LifoQueue       
        stack = LifoQueue()   

        def push(data):
            stack.put(data)
        def pop():
            return stack.get()
        
        vertex = self.vertecies[toVertex]
        push(vertex)
        while True:
            if vertex.previous is not None:
                push(vertex.previous)
                vertex = vertex.previous 
            else:
                break
        retval = []
        while not stack.empty():
            retval.append(pop())
        return retval

    def getPathAsString(self, fromVertex, toVertex):
        vertecies = self.getPath(fromVertex, toVertex)
        retval = ''
        for i in range(0,len(vertecies)):
            retval += vertecies[i].name + ' '
            if i < len(vertecies) - 1:
                retval += '--> '
        return retval

    def resetGraph(self):
        for v in self.vertecies:
            vertex = self.vertecies[v]
            vertex.previous = None
            vertex.distance = None
            vertex.visited = False
            vertex.indegree = 0
            vertex.known = False

    def Dijkstra(self, startVertexName):
        # Check to see that startvertex is in Graph
        if startVertexName not in self.vertecies:
            raise KeyError("Start node not present in graph")
        # Reset visited and previous pointer before running algorithm
        self.resetGraph()
        
        vertex = self.vertecies[startVertexName]
        vertex.distance = distance = weight = 0
        previous_node = None
        #
        # Create priority queue, priority = current weight on edge ...
        # No duplicate edges in queue allowed
        #
        edge = Edge(0, vertex)
        
        from queue import PriorityQueue       
        priqueue = PriorityQueue()
        
        def enqueue(data):
            priqueue.put(data)  
            
        def dequeue():
            return priqueue.get() 
        
        enqueue(edge)
        while not priqueue.empty():
            # Get the element with lowest priority (i.e. weight on edge) 
            edge = dequeue()
            eyeball = edge.vertex
            # If not visited previously, we need to define the distance
            if not eyeball.known:
                eyeball.distance = distance
                eyeball.previous = previous_node
            eyeball.known = True

            # If the vertex pointed to by the edge has an adjecency list, we need to iterate on it
            for adjecentedge in eyeball.adjecent:
                if not adjecentedge.vertex.known:
                    adjecentedge.vertex.distance = eyeball.distance + adjecentedge.weight
                    adjecentedge.vertex.previous = eyeball
                    adjecentedge.vertex.known = True
                    enqueue(adjecentedge)
                else:
                    if adjecentedge.vertex.distance > eyeball.distance + adjecentedge.weight:
                        adjecentedge.vertex.distance = eyeball.distance + adjecentedge.weight
                        adjecentedge.vertex.previous = eyeball
                        enqueue(adjecentedge)        
    
    def topologicalSort(self):
        self.resetGraph()
        # Inspecting all vertecies for verticies that have no incoming edges ...
        for v in self.vertecies:
            vertex = self.vertecies[v]
            for edge in vertex.adjecent:
                self.vertecies[edge.vertex.name].indegree += 1
        # Create a FIFO-queue and define enqueue / dequeue
        from queue import SimpleQueue       
        queue = SimpleQueue()  

        def enqueue(data):
            queue.put(data)
        def dequeue():
            return queue.get()
        
        # Putting vertecies with indegree == 0 onto queue
        for v in self.vertecies:
            if self.vertecies[v].indegree == 0:
                enqueue(self.vertecies[v])
            
        # Logically remove incoming edges ...
        # and preserve sequence ...
        topologicalSequence = []  
        while True:
            if queue.empty():
                break
            vertex = dequeue()
            topologicalSequence.append(vertex)
            for edge in vertex.adjecent:
                edge.vertex.indegree -= 1
                if edge.vertex.indegree == 0:
                    enqueue(edge.vertex)
        
        if len(self.vertecies) != len(topologicalSequence):
            raise Exception("Graph is loopy ...")
        else:
            return topologicalSequence
            
    def DAGShortWeightedPath(self):
        self.resetGraph()
        # Inspecting all vertecies for verticies that have no incoming edges ...
        for v in self.vertecies:
            vertex = self.vertecies[v]
            for edge in vertex.adjecent:
                self.vertecies[edge.vertex.name].indegree += 1
        # Create a FIFO-queue and define enqueue / dequeue
        from queue import SimpleQueue       
        queue = SimpleQueue()  

        def enqueue(data):
            queue.put(data)
        def dequeue():
            return queue.get()
        
        # Putting vertecies with indegree == 0 onto queue
        for v in self.vertecies:
            if self.vertecies[v].indegree == 0:
                enqueue(self.vertecies[v])
                self.vertecies[v].distance = 0
            
        # Logically remove incoming edges ...
        # and update weight 
        while not queue.empty():
            eyeball = dequeue()
            eyeball.known = True
            # If an adjecency list is present, we need to iterate on it
            for edge in eyeball.adjecent:
                edge.vertex.indegree -= 1
                # Updating info based on edges
                if not edge.vertex.known:
                    edge.vertex.distance = eyeball.distance + edge.weight
                    edge.vertex.previous = eyeball
                    edge.vertex.known = True
                else:
                    if edge.vertex.distance > eyeball.distance + edge.weight:
                        edge.vertex.distance = eyeball.distance + edge.weight
                        edge.vertex.previous = eyeball
                        
                if edge.vertex.indegree == 0:
                    enqueue(edge.vertex)


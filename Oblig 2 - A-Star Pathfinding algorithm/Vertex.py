from Edge import Edge

class Vertex():
    
    def __init__(self, name, adjecencyList = []):
        self.name = name
        self.adjecent = adjecencyList
        self.distance = None
        self.previous = None
        self.known = False
        self.indegree = 0
        #
        # Adding A-Star properties ...
        #
        self.g = 0
        self.h = 0
        self.f = 0
        #
        # And a function returning x,y reference based on name of vertex being xnym where n and m are numbers
        #

    def __iter__(self):
        return self
            
    def __lt__(self, other):
        if other:
            if isinstance(other, Vertex):
                return self.f < other.f
        else:
            return False            
    
    def __le__(self, other):
        if other:
            if isinstance(other, Vertex):
                return self.f <= other.f
        else:
            return False            
               
    def __gt__(self, other):
        if other:
            if isinstance(other, Vertex):
                return self.f > other.f
        else:
            return False            
    
    def __ge__(self, other):
        if other:
            if isinstance(other, Vertex):
                return self.f >= other.f
        else:
            return False            

    def position(self):
        # remnove "x" from the string
        s = self.name.split('x')
        pos = s[1].split('y')
        return int(pos[0]), int(pos[1])   
        
    @property 
    def f(self):
        return self.__f
    
    @f.setter
    def f(self, value):
        self.__f = value
        
    @property 
    def g(self):
        return self.__g
    
    @g.setter
    def g(self, value):
        self.__g = value
    
    @property 
    def h(self):
        return self.__h
    
    @h.setter
    def h(self, value):
        self.__h = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
     
    @property
    def adjecent(self):
        return self.__adjecencylist
    
    @adjecent.setter
    def adjecent(self, adjecencylist):
        self.__adjecencylist = adjecencylist

    @property
    def distance(self):
        return self.__distance
    
    @distance.setter
    def distance(self, distance):
        self.__distance = distance
        
    @property
    def previous(self):
        return self.__previous
    
    @previous.setter
    def previous(self, previous_node):
        self.__previous = previous_node

    @property
    def known(self):
        return self.__known
    
    @known.setter
    def known(self, known):
        self.__known = known

    @property
    def indegree(self):
        return self.__indegree
    
    @indegree.setter
    def indegree(self, indegree):
        self.__indegree = indegree
        
        

    def add_adjecent_edge(self,edge = None):
        if edge:
            if isinstance(edge, Edge):
                if self.adjecent == []:
                    self.adjecent = [edge]
                else:    
                    self.adjecent.append(edge)
            else:
                raise TypeError("Attempt to add something in " + \
                                "adjecencylist which is not an edge")
    
    def __str__(self):
        retval = str(self.name) + ': ['
        for e in self.adjecent:
            retval += e.vertex.name + '(' + str(e.weight) + ') '
        retval += '](known = ' + str(self.known) + ')(distance = ' + str(self.distance) + ')'
        if self.distance:
            retval += '(previous=\'' + str(self.previous.name) + '\')'
        retval += '(indegree=\'' + str(self.indegree) + '\')'
        return retval
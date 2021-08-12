class Edge():
    
    def __init__(self, weight, vertex):
        self.vertex = vertex
        self.weight = weight

    @property
    def vertex(self):
        return self.__vertex
    
    @vertex.setter
    def vertex(self, vertex):
        self.__vertex = vertex
     
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        self.__weight = weight
        
    def __str__(self):
        return "(" + str(self.weight) + ") -> " + str(self.vertex.name)
    '''
    def __eq__(self, other):
        if other:
            if isinstance(other, Edge):
                return self.weight == other.weight
        else:
            return False            
    '''
    def __ne__(self, other):
        if other:
            if isinstance(other, Edge):
                return self.weight != other.weight
        else:
            return False            
        
    def __lt__(self, other):
        if other:
            if isinstance(other, Edge):
                return self.weight < other.weight
        else:
            return False            
    
    def __le__(self, other):
        if other:
            if isinstance(other, Edge):
                return self.weight <= other.weight
        else:
            return False            
               
    def __gt__(self, other):
        if other:
            if isinstance(other, Edge):
                return self.weight > other.weight
        else:
            return False            
    
    def __ge__(self, other):
        if other:
            if isinstance(other, Edge):
                return self.weight >= other.weight
        else:
            return False            
        
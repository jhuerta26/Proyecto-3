class Node:

    def __init__(self,id):
        """
        Constructor
        :param id: node identifier
        """
        self.id=id
        self.attr = {
            "edges":[],
            "neighbors":[],
            "geoX_Y":[],
            #Auxiliar para BFS
            "visitedBFS":False,
            #axiliares para DFS
            "visitedDFSI":False,
            "rootNodeDFSI":-1,
            #Auxiliares para algoritmo Dijkstra
            "parent":None,
            "distance":float('inf'),
            "edgeWeight":float('inf'),
        }
    
    def __str__(self):
        """
        Convert node to str
        """
        return str(self.id) + str(self.attr["neighbors"])
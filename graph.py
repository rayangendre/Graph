from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.visited = False
        self.color = ''

    def add_connection(self, vert_obj):
        self.adjacent_to.append(vert_obj)


class Graph:
    '''Add additional helper methods if necessary.'''

    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''

        self.graph = {}

        try:
            with open(filename) as reader_file:
                for line in reader_file:
                    values = line.split()
                    self.add_vertex(values[0])
                    self.add_vertex(values[1])
                    self.add_edge(values[0], values[1])
        except:
            raise FileNotFoundError

        # This method should call add_vertex and add_edge

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if not self.in_graph(key):
            self.graph[key] = Vertex(key)

    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''

        vertex1 = self.get_vertex(v1)
        vertex2 = self.get_vertex(v2)

        vertex1.add_connection(vertex2)
        vertex2.add_connection(vertex1)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        return self.graph.get(key)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        keysss = list(self.graph.keys())
        keysss.sort()

        return keysss

    def in_graph(self, key):
        value = self.graph.get(key)

        if value:
            return True

        return False

    def conn_components(self):
        '''Return a list of lists.  For example: if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.'''

        # This method MUST use Depth First Search logic!
        conn_list = []

        # reset all values to not visited
        list_key = self.graph.keys()
        for y in list_key:
            self.graph.get(y).visited = False

        for v in list_key:
            vertex = self.graph.get(v)
            if vertex.visited is False:
                conn_list.append(self.dfs_helper(vertex))

        sorted_list = sorted(conn_list, key=lambda x: x[0])

        return sorted_list

    def dfs_helper(self, vertex):
        s = Stack(len(self.graph))
        part = []

        s.push(vertex)
        vertex.visited = True

        while not s.is_empty():
            vert = s.pop()

            for value in vert.adjacent_to:
                if value.visited == False:
                    value.visited = True
                    s.push(value)
            part.append(vert.id)

        part.sort()

        return part

    def is_bipartite(self):
        '''Return True if the graph is bicolorable and False otherwise.'''
        # This method MUST use Breadth First Search logic!
        tf_list = []
        list_keys = self.graph.keys()
        for y in list_keys:
            self.graph.get(y).visited = False

        for v in list_keys:
            vertex = self.graph.get(v)
            if vertex.visited is False:
                tf_list.append(self.bipartite_helper(vertex))

        for t in tf_list:
            if t is False:
                return False
        return True

    def bipartite_helper(self, vertex):

        q = Queue(len(self.graph))
        q.enqueue(vertex)
        vertex.visited = True

        while not q.is_empty():
            vert = q.dequeue()

            if vert.color == '':
                vert.color = 'r'

            for v in vert.adjacent_to:
                if v.color == vert.color:
                    return False

                elif v.color == '':
                    if vert.color == 'r':
                        v.color = 'b'
                    if vert.color == 'b':
                        v.color = 'r'
                if v.visited is False:
                    q.enqueue(v)
                    v.visited = True

        return True


'''g = Graph('test1.txt')
vlist = g.get_vertices()
without_v = [x[1:] for x in vlist]
print(without_v)
'''

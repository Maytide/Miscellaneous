import random

class Edge():
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

class Graph():
    def __init__(self, edges, V, E):
        self.edges = edges
        self.V = V
        self.E = E

# ---------------------------------

def karger_min_cut(graph):

    

    return

# ---------------------------------

def create_graph(V, E, edge_list):
    assert E == len(edge_list)
    edges = [Edge(a, b) for a, b in edge_list]
    graph = Graph(edges, V, E)

    return graph

def create_graph_from_file(fname):
    vertices = set()
    E = 0
    edge_list = []
    with open(fname) as f:
        for line in f.readlines():
            a, b = line.split(' ')
            edge_list.append((int(a), int(b)))
            E += 1
            if a not in vertices:
                vertices.add(a)
            if b not in vertices:
                vertices.add(b)
    
    return len(vertices), E, edge_list

# ---------------------------------

n = 10
# V, E = 4, 5
# edge_list = [(0,1), (0,2), (0,3), (1,3), (2,3)]
V, E, edge_list = create_graph_from_file('facebook_combined.txt')
min_cut = E

g = create_graph(V, E, edge_list)

for i in range(n):
    cut = karger_min_cut(g)
    print("Cut found by Karger's randomized algo is %d\n"
           % cut)
    if cut < min_cut:
        min_cut = cut
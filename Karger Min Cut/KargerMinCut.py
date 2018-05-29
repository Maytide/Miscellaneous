# Karger Min Cut C -> Python
# Reference implementation:
# https://www.geeksforgeeks.org/kargers-algorithm-for-minimum-cut-set-1-introduction-and-implementation/
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

class Subset():
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

    # Check equality by object, not by object attributes
    # def __eq__(self, other):
    #     return self.parent == other.parent and \
    #             self.rank == other.rank

    # def __ne__(self, other):
    #     return not self == other

def karger_min_cut(graph):
    V, E, edges = graph.V, graph.E, graph.edges

    subsets = [Subset(i, 0) for i in range(V)]

    num_vertices = V

    while num_vertices > 2:
        i = random.randint(0, E-1)
        subset1 = find(subsets, edges[i].src)
        subset2 = find(subsets, edges[i].dest)

        if subset1 == subset2: continue
        
        print('Contracting edge %d-%d' % (edges[i].src, edges[i].dest))
        num_vertices -= 1
        union(subsets, subset1, subset2)

    cutedges = 0
    for i in range(E):
        subset1 = find(subsets, edges[i].src)
        subset2 = find(subsets, edges[i].dest)
        if subset1 != subset2:
            cutedges += 1
    
    return cutedges

# Disjoint set data structures.
# Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
def find(subsets, i):

    # Path compression
    if subsets[i].parent != i:
        subsets[i].parent \
            = find(subsets, subsets[i].parent)
    
    return subsets[i].parent

def union(subsets, x, y):
    xroot = find(subsets, x)
    yroot = find(subsets, y)

    if subsets[xroot].rank < subsets[yroot].rank:
        subsets[xroot].parent = yroot
    elif subsets[xroot].rank > subsets[yroot].rank:
        subsets[yroot].parent = xroot
    else:
        subsets[yroot].parent = xroot
        subsets[xroot].rank += 1

def create_graph(V, E, edge_list):
    assert E == len(edge_list)
    edges = [Edge(a, b) for a, b in edge_list]
    graph = Graph(edges, V, E)

    return graph

n = 10
V, E = 4, 5
edge_list = [(0,1), (0,2), (0,3), (1,3), (2,3)]
min_cut = E

g = create_graph(V, E, edge_list)

for i in range(n):
    cut = karger_min_cut(g)
    print("Cut found by Karger's randomized algo is %d\n"
           % cut)
    if cut < min_cut:
        min_cut = cut




# Karger Min Cut C -> Python
# THIS IS NOT AN ORIGINAL IMPLEMENTATION!
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
    
    def print(self):
        for edge in self.edges:
            print(edge)

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
        print(subset1, subset2)
        if subset1 == subset2: continue
        
        print('Contracting edge %d-%d' % (edges[i].src, edges[i].dest))
        print('Remaining vertices: %d' % (num_vertices))
        num_vertices -= 1
        union(subsets, subset1, subset2)

    cutedges = 0
    sg1_edge_list = set()
    sg2_edge_list = set()
    sg1_parent = None
    for i in range(E):
        subset1 = find(subsets, edges[i].src)
        subset2 = find(subsets, edges[i].dest)
        if subset1 != subset2:
            cutedges += 1
        else:
            if len(sg1_edge_list) == 0:
                sg1_edge_list.add(edges[i])
                sg1_parent = subset1
            elif len(sg1_edge_list) > 0:
                if sg1_parent == subset1 == subset2:
                    sg1_edge_list.add(edges[i])
                else:
                    sg2_edge_list.add(edges[i])

    return cutedges, sg1_edge_list, sg2_edge_list

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

def node_map(edge_list):
    node_counter = 0
    enumerated_edge_list = [] # List of edges, with nodes mapped from zero -> num_nodes-1
    enumeration_map_fwd = {}
    enumeration_map_inv = {}
    for a, b in enumerate(edge_list):
        if a not in enumeration_map_fwd:
            enumeration_map_fwd[a] = node_counter
            enumeration_map_inv[node_counter] = a
            node_counter += 1

        if b not in enumeration_map_fwd:
            enumeration_map_fwd[b] = node_counter
            enumeration_map_inv[node_counter] = b
            node_counter += 1
        
        enumerated_edge_list.append((enumeration_map_fwd[a], enumeration_map_fwd[b])) 
        
    return enumerated_edge_list, enumeration_map_inv, node_counter

# edge_list = set([(0,1), (0,2), (0,3), (1,3), (2,3)])
edge_list = [
    (1, 2), (1, 5), (1, 6),
    (2, 3), (2, 5), (2, 6),
    (3, 4), (3, 7), (3, 8),
    (4, 7), (4, 8),
    (5, 6),
    (6, 7),
    (7, 8)
]

# edge_list = [list(edge) for edge in edge_list]
# for i in range(len(edge_list)):
#     edge_list[i][0] -= 1
#     edge_list[i][1] -= 1

edge_list, enumeration_map_inv, num_nodes = node_map(edge_list)
print(edge_list)

V, E = 8, len(edge_list)
# V, E, edge_list = create_graph_from_file('facebook_combined.txt')
min_cut = E

g = create_graph(V, E, edge_list)

n = 30
for i in range(n):
    cut, sg1, sg2 = karger_min_cut(g)
    print("Cut found by Karger's randomized algo is %d\n"
           % cut)
    print('subgraph1:', sg1)
    print('subgraph2:', sg2)

    if cut < min_cut:
        min_cut = cut




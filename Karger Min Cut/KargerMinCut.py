# Karger Min Cut C -> Python
# THIS IS NOT AN ORIGINAL IMPLEMENTATION!
# Reference implementation:
# https://www.geeksforgeeks.org/kargers-algorithm-for-minimum-cut-set-1-introduction-and-implementation/
import random


# class Edge():
#     def __init__(self, src, dest):
#         self.src = src
#         self.dest = dest

class Graph():
    def __init__(self, edges, V, E):
        self.edges = edges
        self.V = V
        self.E = E

    # def is_highly_connected(self):
    #     return self.E / 2 <= self.V
    
    def print(self):
        for edge in self.edges:
            print(edge)

class Subset():
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

def karger_min_cut(graph, verbose=False):
    V, E, edges = graph.V, graph.E, graph.edges

    subsets = [Subset(i, 0) for i in range(V)]

    num_vertices = V

    while num_vertices > 2:
        i = random.randint(0, E-1)
        subset1 = find(subsets, edges[i][0])
        subset2 = find(subsets, edges[i][1])
        
        if subset1 == subset2: 
            # print('Trying to find two nodes in diff subsets:', num_vertices, edges[i][0], edges[i][1])
            continue

        num_vertices -= 1
        if num_vertices % 250 == 0 and verbose:
            print(num_vertices)
        union(subsets, subset1, subset2)

    cutedges = 0
    sg1_edge_list = []
    sg2_edge_list = []
    sg1_edge_list_parent = None
    for i in range(E):
        subset1 = find(subsets, edges[i][0])
        subset2 = find(subsets, edges[i][1])
        if subset1 != subset2:
            cutedges += 1
        else:
            if len(sg1_edge_list) == 0:
                sg1_edge_list.append(edges[i])
                sg1_edge_list_parent = subset1
            elif len(sg1_edge_list) > 0:
                if sg1_edge_list_parent == subset1 == subset2:
                    sg1_edge_list.append(edges[i])
                else:
                    sg2_edge_list.append(edges[i])

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
    edges = [(a, b) for a, b in edge_list if a != b]
    graph = Graph(edges, V, E)

    return graph

def create_graph_from_file(fname):
    vertices = set()
    E = 0
    edge_list = []
    with open(fname) as f:
        for line in f.readlines():
            if line.strip()[0] == '#':
                continue
            a, b = line.split()
            # print(a, b)
            if a != b: 
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
    for a, b in edge_list:
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

def merge_graphs(e1, e2):
    # enumerated_edge_list, _, node_counter = node_map(e1 + e2)
    node_counter = 0
    enumerated_edge_list = [] # List of edges, with nodes mapped from zero -> num_nodes-1
    enumeration_map_fwd = {}
    for a, b in e1:
        if a not in enumeration_map_fwd:
            enumeration_map_fwd[a] = node_counter
            node_counter += 1

        if b not in enumeration_map_fwd:
            enumeration_map_fwd[b] = node_counter
            node_counter += 1

        enumerated_edge_list.append((enumeration_map_fwd[a], enumeration_map_fwd[b])) 

    # Don't reset node counter
    enumeration_map_fwd = {}
    for a, b in e2:
        if a not in enumeration_map_fwd:
            enumeration_map_fwd[a] = node_counter
            node_counter += 1

        if b not in enumeration_map_fwd:
            enumeration_map_fwd[b] = node_counter
            node_counter += 1

        enumerated_edge_list.append((enumeration_map_fwd[a], enumeration_map_fwd[b])) 

    return enumerated_edge_list, node_counter


def mincut(g, n=25):
    min_cut = g.E
    min_g1 = None
    min_g2 = None
    sg1_enumeration_map_inv = None
    sg2_enumeration_map_inv = None
    
    for i in range(n):
        # print('Iteration i:', i, min_cut)
        cut, sg1_edge_list, sg2_edge_list = karger_min_cut(g, verbose=False)
        # print("Cut found by Karger's randomized algo is %d\n"
        #        % cut)
        # print('subgraph1:', sg1_edge_list)
        # print('subgraph2:', sg2_edge_list)

        if cut <= min_cut:
            min_cut = cut
            sg1_enumerated_edge_list, sg1_enumeration_map_inv, sg1_node_counter \
                = node_map(sg1_edge_list)
            # g1 = Graph(sg1_enumerated_edge_list, sg1_node_counter, len(sg1_enumerated_edge_list))
            
            sg2_enumerated_edge_list, sg2_enumeration_map_inv, sg2_node_counter \
                = node_map(sg2_edge_list)

            # print('new best sg1:', sg1_enumerated_edge_list[:10])
            # print('new best sg2:', sg2_enumerated_edge_list[:10])
            min_g1 = Graph(sg1_enumerated_edge_list, sg1_node_counter, len(sg1_enumerated_edge_list))
            min_g2 = Graph(sg2_enumerated_edge_list, sg2_node_counter, len(sg2_enumerated_edge_list))
            if min_cut < 2:
                break
    
    return min_cut, min_g1, min_g2, sg1_enumeration_map_inv, sg2_enumeration_map_inv

if __name__ == '__main__':
    # edge_list = set([(0,1), (0,2), (0,3), (1,3), (2,3)])
    # -----------------------------
    # edge_list = [
    #     (1, 2), (1, 5), (1, 6),
    #     (2, 3), (2, 5), (2, 6),
    #     (3, 4), (3, 7), (3, 8),
    #     (4, 7), (4, 8),
    #     (5, 6),
    #     (6, 7),
    #     (7, 8)
    # ]
    # V, E = 8, len(edge_list)
    # edge_list, enumeration_map_inv, num_nodes = node_map(edge_list)
    # -----------------------------
    e1 = [
        (1, 2), (1, 5), (1, 6),
        (2, 3), (2, 5), (2, 6),
        (3, 4), (3, 7), (3, 8),
        (4, 7), (4, 8),
        (5, 6),
        (6, 7),
        (7, 8),
    ]
    e2 = [
        (1, 2), (1, 5), (1, 6),
        (2, 3), (2, 5), (2, 6),
        (3, 4), (3, 7), (3, 8),
        (4, 7), (4, 8),
        (5, 6),
        (6, 7),
        (7, 8),
    ]
    edge_list, V = merge_graphs(e1, e2)
    edge_list.extend([
        (0, 7),
        (2, 9),
        (4, 10),
        (8, 11)
    ])
    E = len(edge_list)
    print(edge_list)
    # -----------------------------
    # V, E, edge_list = create_graph_from_file('as20000102.txt')
    # V, E, edge_list = create_graph_from_file('facebook_combined.txt')
    # edge_list, enumeration_map_inv, num_nodes = node_map(edge_list)
    # -----------------------------

    print(edge_list[:10])
    g = create_graph(V, E, edge_list)
    mincut(g)

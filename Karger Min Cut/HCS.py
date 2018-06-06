from KargerMinCut import *


def is_highly_connected(g, min_cut):
    return min_cut >= g.E/2


def HCS(g):
    print(g.E, g.V)
    # if g.is_highly_connected():
    #     g.print()
    
    min_cut, h1, h2, inv_map1, inv_map2 = mincut(g)
    if is_highly_connected(g, min_cut):
        g.print()
        return g

    HCS(h1)
    HCS(h2)

if __name__ == '__main__':
    e1 = [
        (1, 2), (1, 5), (1, 6),
        (2, 3), (2, 5), (2, 6),
        (3, 4), (3, 7), (3, 8),
        (4, 7), (4, 8),
        (5, 6),
        (6, 7),
        (7, 8),
    ]
    # edge_list, inv_map, V = node_map(e1)
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
    g = create_graph(V, E, edge_list)
    HCS(g)
# TODO: Implement code to generate Python dict from list of tuples generate dict

def build_graph_as_dict(node_list, isDirectedGraph):
    '''
    Write a function to create a python dictionary implementation of a directed/undirected graph from a node-list.
    create map - node -> [child, child]
    :param node_list: [('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('A', 'E'), ('B', 'F')]
    :param isDirectedGraph: True or False
    :return: {'A': ['B', 'E'], 'B': ['A', 'C', 'F'], 'C': ['B', 'D', 'E'], 'D': ['C'], 'E': ['C', 'A'], 'F': ['B']}
    '''
    node_map = {}

    for tup in node_list:
        n1, n2 = tup

        if n1 in node_map:
            children = node_map[n1]
            node_map[n1] = children + [n2]
        else:
            node_map[n1] = [n2]


        if not isDirectedGraph:
            if n2 in node_map:
                children = node_map[n2]
                node_map[n2] = children + [n1]
            else:
                node_map[n2] = [n1]

    return node_map



def build_graph_as_dict(node_list, isDirected=True):
    '''
    :param node_list:
    :param isDirected:
    create a node map - node -> [child, child]

    :return node_map:
    '''
    node_map = {}
    for tup in node_list:
        n1, n2 = tup
        print(f'n1: {n1}')
        print(f'n2: {n2}')
        if n1 in node_map.keys():
            node_map[n1].append(n2)
        else:
            node_map[n1] = [n2]

        if not isDirected:
            if n2 in node_map.keys():
                node_map[n2].append(n1)
            else:
                node_map[n2] = [n1]

        print(f'node_map: {node_map}')

    return node_map

if __name__ == "__main__":
    # Test case 1: Undirected graph
    node_list1 = [(1, 2), (2, 3), (3, 1)]
    node_map1 = build_graph_as_dict(node_list1, isDirected=False)
    print("Test case 1 (Undirected graph):", node_map1)
    print()

    # Test case 2: Directed graph
    node_list2 = [(1, 2), (2, 3), (3, 1)]
    node_map2 = build_graph_as_dict(node_list2, isDirected=True)
    print("Test case 2 (Directed graph):", node_map2)
    print()

    # Test case 3: Directed graph with a self-loop
    node_list3 = [(1, 1), (2, 2), (3, 3)]
    node_map3 = build_graph_as_dict(node_list3, isDirected=True)
    print("Test case 3 (Directed graph with self-loop):", node_map3)
    print()

    # Test case 4: Empty input
    node_list4 = []
    node_map4 = build_graph_as_dict(node_list4, isDirected=True)
    print("Test case 4 (Empty input):", node_map4)
    print()
import numpy as np

def gen_matrix_and_map_from_node_list(node_list, isDirected=False):
    '''
    :param node_list:
    :param isDirected:
    :return: matrix, node_map
    '''
    node_set = set()

    for tup in node_list:
        n1, n2 = tup
        node_set.add(n1)
        node_set.add(n2)
    print(f'node_set: {node_set}')

    dim = len(node_set)
    matrix = np.zeros((dim,dim), dtype=int)
    print(f'matrix: {matrix}')

    sorted_node_list = sorted(node_set)
    print(f'sorted_node_list: {sorted_node_list}')
    node_map = {}
    idx = 0
    for node in sorted_node_list:
        node_map[node] = idx
        idx += 1
    print(f'node_map: {node_map}')

    for tup in node_list:
        n1, n2 = tup
        n1_idx = node_map[n1]
        n2_idx = node_map[n2]
        print(f'n1: {n1}')
        print(f'n2: {n2}')
        print(f'n1_idx: {n1_idx}')
        print(f'n2_idx: {n2_idx}')

        matrix[n1_idx][n2_idx] = 1

        if not isDirected:
            matrix[n2_idx][n1_idx] = 1

        print(f'matrix: {matrix}')

    return matrix, node_map


def get_children_row_idx(node, matrix, node_map):
    children_row_idx = []
    node_idx = node_map[node]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != node_idx:
                continue
            if matrix[i][j] != 0:
                children_row_idx.append(i)

    return children_row_idx


def main_build_matrix():
    node_list = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('A', 'E'), ('B', 'F')]
    matrix, node_map = gen_matrix_and_map_from_node_list(node_list, False)
    print(matrix)

    print(node_map)
    print('node_list:\n', node_list)

    # get children of 'B'
    children_row_idxs = get_children_row_idx('B', matrix, node_map)
    print(f'children_row_idxs: {children_row_idxs}')


if __name__ == "__main__":
    # Test case 1: Undirected graph
    node_list1 = [(1, 2), (2, 3), (3, 1)]
    matrix1, node_map1 = gen_matrix_and_map_from_node_list(node_list1, isDirected=False)
    print("Test case 1 (Undirected graph):")
    print(f"Adjacency Matrix: {matrix1}")
    print(f"Node Map: {node_map1}")
    print()


    # Test case 2: Directed graph
    node_list2 = [(1, 2), (2, 3), (3, 1)]
    matrix2, node_map2 = gen_matrix_and_map_from_node_list(node_list2, isDirected=True)
    print("Test case 2 (Directed graph):")
    print(f"Adjacency Matrix: {matrix2}")
    print(f"Node Map: {node_map2}")
    print()

    # Test case 3: Directed graph with a self-loop
    node_list3 = [(1, 1), (2, 2), (3, 3)]
    matrix3, node_map3 = gen_matrix_and_map_from_node_list(node_list3, isDirected=True)
    print("Test case 3 (Directed graph with self-loop):")
    print(f"Adjacency Matrix: {matrix3}")
    print(f"Node Map: {node_map3}")
    print()

    # Test case 4: Empty input
    node_list4 = []
    matrix4, node_map4 = gen_matrix_and_map_from_node_list(node_list4, isDirected=True)
    print("Test case 4 (Empty input):")
    print(f"Adjacency Matrix: {matrix4}")
    print(f"Node Map: {node_map4}")
    print()

    main_build_matrix()



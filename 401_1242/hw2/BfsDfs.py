# HW2  - Compare BFS DFS search algorithms
# todo: 0. replace the function build_graph_as_dict with your code from hw2
# todo: 1. add code to count number of nodes visited for both bfs and dfs
#            hint: define global variables and display the result
# todo: 2. modify bfs to handle iterative deepening
# todo: 3. Write shortest path functions that return shortest path\
#          using BFS and DFS with iterative deepening
#


def build_graph_as_dict (node_list, directed=True):
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

        if not directed:
            if n2 in node_map:
                children = node_map[n2]
                node_map[n2] = children + [n1]
            else:
                node_map[n2] = [n1]

    return node_map


def bfs_all_paths(graph, start, goal):
    queue = [(start, [start])]
    global bfs_node_count
    bfs_node_count = 0

    while queue:
        (vertex, path) = queue.pop(0)
        bfs_node_count += 1
        next_node_list = [x for x in graph[vertex] if x not in set(path)]
        for next in next_node_list:
            if next == goal:
                yield path + [next]
            else:
                queue.append( (next, path + [next]))
    return None


def dfs_all_paths(graph, start, goal):
    stack = [(start, [start])]
    global dfs_node_count
    dfs_node_count = 0

    while stack:
        # note pop()  returns LAST value in list
        (vertex, path) = stack.pop()
        dfs_node_count += 1
        next_node_list = [x for x in graph[vertex] if x not in set(path)]
        for next in next_node_list:
            if next == goal:
                yield path + [next]
            else:
                stack.append( (next, path + [next]))
    return None




# main - try with larger graph and measure memory/search - complex graph ?
def main():
    # small graph - using integers for node labels
    node_list_1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]

    # larger graph
    node_list_2 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (100, 101), (101, 102), (102, 103), (103, 104), (104, 105), (105, 106), (106, 107), (107, 108), (108, 109), (109, 110), (110, 111), (111, 112), (112, 113), (113, 114), (114, 115), (115, 116), (116, 117), (117, 118), (118, 119), (119, 120), (4, 100), (120, 10), (200, 201), (201, 202), (202, 203), (203, 204), (204, 205), (205, 206), (206, 207), (207, 208), (208, 209), (209, 210), (210, 211), (211, 212), (212, 213), (213, 214), (214, 215), (215, 216), (216, 217), (217, 218), (218, 219), (219, 220), (1, 200), (220, 10), (300, 301), (301, 302), (302, 303), (303, 304), (304, 305), (305, 306), (306, 307), (307, 308), (308, 309), (309, 310), (310, 311), (311, 312), (312, 313), (313, 314), (314, 315), (315, 316), (316, 317), (317, 318), (318, 319), (319, 320), (3, 300), (320, 10), (106, 200), (220, 112), (10, 666), (10, 667), (10, 668), (668, 669), (666, 668)]

    # create your graph data structure from the node_list
    graph = build_graph_as_dict(node_list_2, directed=False)

    # Here we are using nodes labeled with integers (0,1,2,...)
    print ("\nBreadth First Search-----------")
    start_node = 1
    goal_node = 10

    # get a list of all the paths to goal using BFS
    bfs_path_list  = list(bfs_all_paths(graph, start_node, goal_node))
    bfs_min_path_length = float('inf')
    bfs_min_path = []
    for path in bfs_path_list:
        if len(path) < bfs_min_path_length:
            bfs_min_path_length = len(path)
            bfs_min_path = path
    print(f'bfs shortest path: {bfs_min_path}')
    print(f'bfs_node_count: {bfs_node_count}')


    # display # paths  and the paths
    print (f"BFS all paths. Number paths={len(bfs_path_list)}\nBFS paths: {bfs_path_list}")


    print("\n\nDepth First Search--------------")

    # get a list of all the paths to goal using DFS
    # you need to modify the function to do interative deepening
    # Can you reduce the # of nodes explored by setting a deep level?
    dfs_path_list = list(dfs_all_paths(graph, start_node, goal_node))
    dfs_min_path_length = float('inf')
    dfs_min_path = []
    for path in dfs_path_list:
        if len(path) < dfs_min_path_length:
            dfs_min_path_length = len(path)
            dfs_min_path = path
    print(f'dfs shortest path: {dfs_min_path}')
    print(f'dfs_node_count: {dfs_node_count}')

    # results for DFS
    print (f"DFS all paths. Number paths={len(dfs_path_list)}\nDFS paths: {dfs_path_list}")

# run the main function
main()
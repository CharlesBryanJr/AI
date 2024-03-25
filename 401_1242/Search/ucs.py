from EasyGraph import EasyGraph
from queue import PriorityQueue


def ucs(graph, start, goal):
    # returns shortest path to goal
    visited = []
    queue = PriorityQueue()
    queue.put((0, [start]))  # need to return path so track list of nodes

    while not queue.empty():
        cost, path = queue.get()
        node = path[-1]  # node to explore is last on current path

        if node not in visited:
            visited.append(node)

            if node == goal:
                return (cost, path)  # this will be shortest path

            for child in graph.children(node):
                if child not in visited:
                    total_cost = cost + graph.cost(node, child)
                    queue.put((total_cost, path + [child]))

    return None


if __name__ == "__main__":
    # Test Case 1: Simple Directed Graph
    graph1 = EasyGraph([('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 4)])
    result1 = ucs(graph1, 'A', 'C')
    print("Test Case 1 Result:", result1)

    # Test Case 2: Directed Graph with Multiple Paths
    graph2 = EasyGraph([('A', 'B', 3), ('B', 'C', 5), ('A', 'C', 2), ('C', 'D', 1), ('B', 'D', 4)])
    result2 = ucs(graph2, 'A', 'D')
    print("Test Case 2 Result:", result2)

    # Test Case 3: Undirected Graph
    graph3 = EasyGraph([('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3), ('D', 'A', 4)], undirected=True)
    result3 = ucs(graph3, 'A', 'D')
    print("Test Case 3 Result:", result3)

    # Test Case 4: Graph with No Path to Goal
    graph4 = EasyGraph([('A', 'B', 2), ('B', 'C', 3)])
    result4 = ucs(graph4, 'A', 'D')
    print("Test Case 4 Result:", result4)

import heapq


def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity and the start node as 0.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to keep track of nodes to visit next based on their distances.
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the node with the smallest distance.
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the recorded distance, skip.
        if current_distance > distances[current_node]:
            continue

        # Visit neighbors and update distances.
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage:
if __name__ == "__main__":
    # Define the graph as an adjacency dictionary with edge weights.
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)

    # Print the shortest distances from the start node to all other nodes.
    for node, distance in shortest_distances.items():
        print(f"Shortest distance from {start_node} to {node}: {distance}")

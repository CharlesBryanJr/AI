def get_neighbors(current_pos):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up, right, down, left
    neighbors = []
    for dx, dy in directions:
        next_pos = (current_pos[0] + dx, current_pos[1] + dy)
        neighbors.append(next_pos)
    return neighbors

# Example usage:
current_position = (5, 5)
neighbors = get_neighbors(current_position)
print("Current position:", current_position)
print("Neighbors:", neighbors)

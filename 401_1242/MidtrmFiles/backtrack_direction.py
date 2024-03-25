import random
# Directions are 0=up, 1=right, 2=down, 3=left
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def backtrack_direction(last_pos, pos):
    dx = last_pos[0] - pos[0]
    dy = last_pos[1] - pos[1]
    if dx == -1:
        return 3  # Left
    elif dx == 1:
        return 1  # Right
    elif dy == -1:
        return 0  # Up
    elif dy == 1:
        return 2  # Down
    else:
        print("No path to backtrack to.")
        return random.choice([0, 1, 2, 3])

last_pos = (6, 4)
pos = (6, 4)
print("backtrack direction:", backtrack_direction(last_pos, pos))

last_pos = (6, 4)
pos = (6, 3)
print("backtrack direction:", backtrack_direction(last_pos, pos))

last_pos = (6, 3)
pos = (7, 3)
print("backtrack direction:", backtrack_direction(last_pos, pos))

last_pos = (7, 3)
pos = (6, 3)
print("backtrack direction:", backtrack_direction(last_pos, pos))
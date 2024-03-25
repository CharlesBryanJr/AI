def is_next_pos_valid(next_pos, room_width, room_height, block_tiles_set, visited):
    x, y = next_pos
    return (0 <= x < room_width and 0 <= y < room_height and
            next_pos not in block_tiles_set and next_pos not in visited)

# Test Case 1: Valid position within room boundaries
room_width = 5
room_height = 5
block_tiles_set = {(2, 2), (3, 3)}
visited = {(1, 1), (2, 1)}
next_pos = (3, 4)
print("Test Case 1: Valid position within room boundaries")
print("Expected: True")
print("Actual:", is_next_pos_valid(next_pos, room_width, room_height, block_tiles_set, visited))

# Test Case 2: Invalid position due to being out of room boundaries
next_pos = (-1, 2)
print("\nTest Case 2: Invalid position due to being out of room boundaries")
print("Expected: False")
print("Actual:", is_next_pos_valid(next_pos, room_width, room_height, block_tiles_set, visited))

# Test Case 3: Invalid position due to being on a blocked tile
next_pos = (2, 2)
print("\nTest Case 3: Invalid position due to being on a blocked tile")
print("Expected: False")
print("Actual:", is_next_pos_valid(next_pos, room_width, room_height, block_tiles_set, visited))

# Test Case 4: Invalid position due to already being visited
next_pos = (2, 1)
print("\nTest Case 4: Invalid position due to already being visited")
print("Expected: False")
print("Actual:", is_next_pos_valid(next_pos, room_width, room_height, block_tiles_set, visited))
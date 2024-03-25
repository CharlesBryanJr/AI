def get_opposite_direction(direction):
    opposite_directions = {1: 3, 3: 1, 2: 0, 0: 2}
    return opposite_directions.get(direction, None)


# Test case 1: Moving right, expect to move left to backtrack
forward_direction = 1  # Right
backward_direction = get_opposite_direction(forward_direction)
print(f"Forward: {forward_direction}, Backward: {backward_direction}")  # Should print "Forward: 1, Backward: 3"

# Test case 2: Moving left, expect to move right to backtrack
forward_direction = 3  # Left
backward_direction = get_opposite_direction(forward_direction)
print(f"Forward: {forward_direction}, Backward: {backward_direction}")  # Should print "Forward: 3, Backward: 1"

# Test case 3: Moving down, expect to move up to backtrack
forward_direction = 2  # Down
backward_direction = get_opposite_direction(forward_direction)
print(f"Forward: {forward_direction}, Backward: {backward_direction}")  # Should print "Forward: 2, Backward: 0"

# Test case 4: Moving up, expect to move down to backtrack
forward_direction = 0  # Up
backward_direction = get_opposite_direction(forward_direction)
print(f"Forward: {forward_direction}, Backward: {backward_direction}")  # Should print "Forward: 0, Backward: 2"

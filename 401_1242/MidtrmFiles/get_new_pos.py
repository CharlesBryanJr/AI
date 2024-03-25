def get_new_pos(dir, curr_pos):
    x, y = curr_pos
    if dir == 0:  # Up
        return (x, y - 1)
    elif dir == 1:  # Right
        return (x + 1, y)
    elif dir == 2:  # Down
        return (x, y + 1)
    elif dir == 3:  # Left
        return (x - 1, y)
    else:
        return 'Invalid direction'


# Test case 1: Move up
current_position = (5, 5)
new_position = get_new_pos(0, current_position)
print("Direction: Up")
print("Current position:", current_position)
print("New position:", new_position)

# Test case 2: Move right
current_position = (5, 5)
new_position = get_new_pos(1, current_position)
print("\nDirection: Right")
print("Current position:", current_position)
print("New position:", new_position)

# Test case 3: Move down
current_position = (5, 5)
new_position = get_new_pos(2, current_position)
print("\nDirection: Down")
print("Current position:", current_position)
print("New position:", new_position)

# Test case 4: Move left
current_position = (5, 5)
new_position = get_new_pos(3, current_position)
print("\nDirection: Left")
print("Current position:", current_position)
print("New position:", new_position)

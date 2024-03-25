def calculate_direction(current_pos, next_pos):
    print(f"Calculating direction from current position {current_pos} to next position {next_pos}")

    dx = next_pos[0] - current_pos[0]
    dy = next_pos[1] - current_pos[1]

    print(f"Delta X (dx): {dx}, Delta Y (dy): {dy}")

    if dx == 1:
        print("Moving right")
        return 1  # Right
    elif dx == -1:
        print("Moving left")
        return 3  # Left
    elif dy == 1:
        print("Moving down")
        return 2  # Down
    elif dy == -1:
        print("Moving up")
        return 0  # Up

    print("No valid direction found. Staying in place.")
    print()
    return -1  # Stay or invalid direction


def test_calculate_direction():

    # Test move right
    assert calculate_direction((0, 0), (1, 0)) == 1, "Should move right"

    # Test move left
    assert calculate_direction((1, 0), (0, 0)) == 3, "Should move left"

    # Test move up
    assert calculate_direction((0, 1), (0, 0)) == 0, "Should move up"

    # Test move down
    assert calculate_direction((0, 0), (0, 1)) == 2, "Should move down"

    # Test staying in place
    assert calculate_direction((0, 0), (0, 0)) == -1, "Should stay in place"

    print("All tests passed!")

test_calculate_direction()

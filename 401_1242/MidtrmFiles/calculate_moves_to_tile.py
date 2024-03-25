def calculate_moves_to_tile(pos, next_clean_tile):
    print('')
    print('calculate_moves_to_tile')
    x_distance = next_clean_tile[0] - pos[0]
    y_distance = next_clean_tile[1] - pos[1]
    return x_distance, y_distance


pos_1 = (3, 3)
next_clean_tile_1 = (7, 7)

pos_2 = (0, 0)
next_clean_tile_2 = (10, 10)

pos_3 = (-2, -2)
next_clean_tile_3 = (-5, -5)

x_dist_1, y_dist_1 = calculate_moves_to_tile(pos_1, next_clean_tile_1)
print("Test 1:")
print("X distance:", x_dist_1)
print("Y distance:", y_dist_1)

x_dist_2, y_dist_2 = calculate_moves_to_tile(pos_2, next_clean_tile_2)
print("\nTest 2:")
print("X distance:", x_dist_2)
print("Y distance:", y_dist_2)

x_dist_3, y_dist_3 = calculate_moves_to_tile(pos_3, next_clean_tile_3)
print("\nTest 3:")
print("X distance:", x_dist_3)
print("Y distance:", y_dist_3)
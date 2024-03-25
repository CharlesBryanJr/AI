from math import sqrt

def euclidean_distance(cord_1, cord_2):
    x1, y1 = cord_1
    x2, y2 = cord_2
    row_difference = x2 - x1
    column_difference = y2 - y1
    row_difference_squared = row_difference ** 2
    column_difference_squared = column_difference ** 2
    sum_of_squares = row_difference_squared + column_difference_squared
    distance = sqrt(sum_of_squares)
    return distance


def get_zero_position(array, rows, cols):
    zero_count = 0
    zero_position = None

    for row in range(rows):
        for col in range(cols):
            if array[row][col] == 0:
                zero_count += 1
                zero_position = (row, col)
    if zero_position is None:
        raise ValueError("The array does not contain a zero element.")
    if zero_count > 1:
        raise ValueError("This array contains more than one zero element.")

    return zero_position


start = [[4,1,3],[2,0,6],[7,5,8]]
end = [[1,2,3],[4,5,6],[7,8,0]]

zero_start = get_zero_position(start, len(start), len(start[0]))
zero_end = get_zero_position(end, len(end), len(end[0]))
bottom_right_corner = (2, 2)

distance_start = euclidean_distance(zero_start, bottom_right_corner)
distance_end = euclidean_distance(zero_end, bottom_right_corner)

print(f"Distance in 'start' matrix: {distance_start}")
print(f"Distance in 'end' matrix: {distance_end}")
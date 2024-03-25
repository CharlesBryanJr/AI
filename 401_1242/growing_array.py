def is_square_matrix(matrix, size):
    """Checks if a nested list is a square matrix of a given size."""
    if not isinstance(matrix, list) or len(matrix) != size:
        return False
    for row in matrix:
        if not isinstance(row, list) or len(row) != size:
            return False
    return True

def search_matrix(nested, sizes, last_matrix=None):
    """Recursively searches for the last square matrix of specified sizes in a nested array."""
    if isinstance(nested, list):
        for element in nested:
            for size in sizes:
                if is_square_matrix(element, size):
                    last_matrix = element
                    break
            else:
                last_matrix = search_matrix(element, sizes, last_matrix)
    return last_matrix

def find_last_square_matrix(nested_array, sizes=[3, 4]):
    """Finds the last square matrix of specified sizes in a nested array."""
    return search_matrix(nested_array, sizes)


# Example usage
path = [[[[4, 1, 3], [2, 0, 6], [7, 5, 8]], [[4, 0, 3], [2, 1, 6], [7, 5, 8]]]]
result_matrix = find_last_square_matrix(path)
print(result_matrix)
import copy
from queue import PriorityQueue
from math import sqrt


def get_child_boards_list(board):
    '''
    Returns a list of all the child boards for any given board.
    :param board: x by x array
    :return: [child_boards]
    '''

    rows, cols = is_square_array(board)
    blank_postion = get_zero_position(board, rows, cols)
    child_boards = []

    up_move_child_board = get_up_move_board(board, blank_postion, rows, cols)
    if up_move_child_board is not None:
        child_boards.append(up_move_child_board)
    
    down_move_child_board = get_down_move_board(board, blank_postion, rows, cols)
    if down_move_child_board is not None:
        child_boards.append(down_move_child_board)

    left_move_child_board = get_left_move_board(board, blank_postion, rows, cols)
    if left_move_child_board is not None:
        child_boards.append(left_move_child_board)

    right_move_child_board = get_right_move_board(board, blank_postion, rows, cols)
    if right_move_child_board is not None:
        child_boards.append(right_move_child_board)

    return child_boards


def get_up_move_board(board, blank_postion, rows, cols):
    row, col = blank_postion
    if row == 0:
        return None

    array = copy.deepcopy(board)
    temp = array[row - 1][col]
    array[row - 1][col] = 0
    array[row][col] = temp

    return array


def get_down_move_board(board, blank_postion, rows, cols):
    row, col = blank_postion
    if row == len(board) - 1:
        return None

    array = copy.deepcopy(board)
    temp = array[row + 1][col]
    array[row + 1][col] = 0
    array[row][col] = temp

    return array


def get_left_move_board(board, blank_postion, rows, cols):
    row, col = blank_postion
    if col == 0:
        return None

    array = copy.deepcopy(board)
    temp = array[row][col - 1]
    array[row][col - 1] = 0
    array[row][col] = temp

    return array


def get_right_move_board(board, blank_postion, rows, cols):
    row, col = blank_postion
    if col == cols - 1:
        return None

    array = copy.deepcopy(board)
    temp = array[row][col + 1]
    array[row][col + 1] = 0
    array[row][col] = temp

    return array


def is_square_array(array):
    rows = len(array)
    cols = len(array[0])
    if rows != cols:
        raise ValueError("The board is not a square. Number of rows and columns must be equal.")
    return rows, cols


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


def bfs2(start_board, goal_board):
    queue = [[start_board]]
    global bfs2_counter
    bfs2_counter = 0

    while queue:
        bfs2_counter += 1
        path = queue.pop(0)
        node = path[-1]

        if node == goal_board:
            return path

        child_boards = get_child_boards_list(node)
        for child_board in child_boards:
            if not child_board in path:
                new_path = path + [child_board]
                queue.append(new_path)

    return None


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



def bfs2_euclidean(start_board, goal_board):
    rows, cols = is_square_array(start_board)
    zero_position = get_zero_position(start_board, rows, cols)

    priority_queue = PriorityQueue()
    global bfs2_euclidean_counter
    bfs2_euclidean_counter = 0

    start_dist = euclidean_distance(zero_position, (rows - 1, cols - 1))
    priority_queue.put((start_dist, [start_board]))

    while not priority_queue.empty():
        bfs2_euclidean_counter += 1
        priority, path = priority_queue.get()
        current_board = path[-1]

        child_boards = get_child_boards_list(current_board)
        for child_board in child_boards:
            if child_board == goal_board:
                return path + [child_board]
            else:
                if not child_board in path:
                    new_path = path + [child_board]
                    zero_position = get_zero_position(child_board, rows, cols)
                    dist = euclidean_distance(zero_position, (rows - 1, cols - 1))
                    total_priority = dist + len(new_path)
                    priority_queue.put((total_priority, new_path))

    return None



def manhattan_distance(cord_1, cord_2):
    x1, y1 = cord_1
    x2, y2 = cord_2
    row_difference = abs(x2 - x1)
    column_difference = abs(y2 - y1)
    distance = row_difference + column_difference
    return distance


def bfs2_manhattan(start_board, goal_board):
    rows, cols = is_square_array(start_board)
    zero_position = get_zero_position(start_board, rows, cols)

    priority_queue = PriorityQueue()
    global bfs2_manhattan_counter
    bfs2_manhattan_counter = 0

    start_dist = manhattan_distance(zero_position, (rows - 1, cols - 1))
    priority_queue.put((start_dist, [start_board]))

    while not priority_queue.empty():
        bfs2_manhattan_counter += 1
        priority, path = priority_queue.get()
        current_board = path[-1]

        child_boards = get_child_boards_list(current_board)
        for child_board in child_boards:
            if child_board == goal_board:
                return path + [child_board]
            else:
                if not child_board in path:
                    new_path = path + [child_board]
                    zero_position = get_zero_position(child_board, rows, cols)
                    dist = manhattan_distance(zero_position, (rows - 1, cols - 1))
                    total_priority = dist + len(new_path)
                    priority_queue.put((total_priority, new_path))

    return None


def main():
    print()
    start = [[4,1,3],[2,0,6],[7,5,8]]
    end = [[1,2,3],[4,5,6],[7,8,0]]
    print(f'3x3: {bfs2(start, end)}')
    print(f'bfs2_counter: {bfs2_counter}')
    print('---------------')
    start = [
        [1, 2, 3, 4],
        [5, 7, 6, 8],
        [9, 10, 0, 11],
        [13, 14, 15, 12]
    ]
    end = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]
    print(f'4x4: {bfs2(start, end)}')
    print(f'bfs2_counter_4x4: {bfs2_counter}')
    print('---------------')
    start = [[4,1,3],[2,0,6],[7,5,8]]
    end = [[1,2,3],[4,5,6],[7,8,0]]
    print(f'bfs2_euclidean: {bfs2_euclidean(start, end)}')
    print(f'bfs2_euclidean_counter: {bfs2_euclidean_counter}')
    print('---------------')
    start = [[4,1,3],[2,0,6],[7,5,8]]
    end = [[1,2,3],[4,5,6],[7,8,0]]
    print(f'bfs2_manhattan: {bfs2_manhattan(start, end)}')
    print(f'bfs2_manhattan_counter: {bfs2_euclidean_counter}')
    print()


if __name__ == "__main__":
    main()
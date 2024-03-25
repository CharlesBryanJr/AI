# MiniMax - Get score for board

import math
import numpy as np
import time

from copy import copy
COUNT = 0    # use the COUNT variable to track number of boards explored

def showBoard(board):
    # displays rows of board
    strings = ["" for i in range(board.shape[0])]
    idx = 0
    for row in board:
        for cell in row:
            if cell == 1:
                s = 'X'
            elif cell == -1:
                s = 'O'
            else:
                s = '_'

            strings[idx] += s
        idx += 1

    # display final board
    for s in strings:
        print(s)


def get_board_one_line(board):
    # returns one line rep of a board
    import math
    npb_flat = board.ravel()
    stop = int(math.sqrt(len(npb_flat)))

    bstr = ''
    for idx in range(len(npb_flat)):
        bstr += (str(npb_flat[idx]) + ' ')
        if (idx + 1) % (stop) == 0:
            bstr += '|'
    return bstr


def evaluate(board):
    '''returns 1 for X win, -1 for O win, 0 for tie OR game in progress
    Using numpy functions to add values in rows and cols
    If we get a sum equal to size of row,col,diag (plus or minus)
     we have a winner
    '''
    results = [row_winner(board), column_winner(board), left_diagonal_winner(board), right_diagonal_winner(board)]
    for result in results:
        if result != 0:
            return result
    return 0


def row_winner(board):
    for i in range(3):
        if np.all(board[i, :] == 1):
            return 1
        if np.all(board[i, :] == -1):
            return -1
    return 0


def column_winner(board):
    for i in range(3):
        if np.all(board[:, i] == 1):
            return 1
        if np.all(board[:, i] == -1):
            return -1
    return 0


def left_diagonal_winner(board):
    if np.all(np.diag(board) == 1):
        return 1
    if np.all(np.diag(board) == -1):
        return -1
    return 0


def right_diagonal_winner(board):
    flipped_board = np.fliplr(board)
    if np.all(np.diag(flipped_board) == 1):
        return 1
    if np.all(np.diag(flipped_board) == -1):
        return -1
    return 0


def is_terminal_node(board):
    found_winner = evaluate(board) != 0
    if found_winner:
        return True
    if all_positions_filled(board):
        return True
    return False


def all_positions_filled(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return False
    return True


def get_max_number_child_boards(board):
    zero_count = 0
    for i in board:
        for j in i:
            if j == 0:
                zero_count +=1
    return zero_count


def get_child_boards(board, char):
    player = 1 if char == 'X' else -1
    count_child_boards = 0
    number_child_boards = 0
    max_number_child_boards = get_max_number_child_boards(board)
    child_boards = []
    return a(board, char, player, number_child_boards, max_number_child_boards, child_boards)


def a(board, char, player, number_child_boards, max_number_child_boards, child_boards):
    if number_child_boards >= max_number_child_boards:
        return

    child_board = []
    count_child_boards = 0

    for i in range(len(board)):
        row = []
        for j in range(len(board[i])):
            curr = board[i][j]

            found_existing_move = curr in (-1, 1)
            if found_existing_move:
                row.append(curr)
            else:
                found_new_move = count_child_boards == number_child_boards
                if found_new_move:
                    row.append(player)
                    count_child_boards += 1
                else:
                    row.append(curr)
                count_child_boards += 1

        child_board.append(row)

    child_boards.append(np.array(child_board))
    a(board, char, player, number_child_boards+1, max_number_child_boards, child_boards)
    return child_boards


def minimax(board, depth, maximizingPlayer):
    '''returns the value of the board
       0 (draw) 1 (win for X) -1 (win for O)
       Explores all child boards for this position and returns
       the best score given that all players play optimally
    '''

    global board_count
    board_count += 1

    if depth == 0 or is_terminal_node(board):
        return evaluate(board)

    if maximizingPlayer:  # max player plays X
        maxEva = -math.inf
        child_list = get_child_boards(board, 'X')
        for child_board in child_list:
            eva = minimax(child_board, depth-1, False)
            maxEva = max(maxEva, eva)
        return maxEva

    else:             # minimizing player
        minEva = math.inf
        child_list = get_child_boards(board, 'O')
        for child_board in child_list:
            eva = minimax(child_board, depth - 1, True)
            minEva = min(minEva, eva)
        return minEva


def run_minimax(board):
    global board_count
    board_count = 0

    # set max_depth to the number of blanks (zeros) in the board
    max_depth = np.count_nonzero(board==0)
    print(f"Running minimax w/ max depth {max_depth} for:")
    showBoard(board)
    board_sum = np.sum(board)
    if board_sum == 0:
        is_x_to_move = True
    elif board_sum == 1:
        is_x_to_move = False
    else:
        raise ValueError("Invalid board state: The sum of the board should be 0 or 1.")

    start_time = time.time()
    score = minimax(board, max_depth, is_x_to_move)
    end_time = time.time()
    time_elapsed = end_time - start_time

    return score, board_count, time_elapsed


board_count = 0


def run_code_tests():
    '''
    b1 : expect win for X (1)  < 200 boards explored
    b1 = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])

    In addtion to the board b1, run tests on the following
    boards:
       b2:  expect win for O (-1)  > 1000 boards explored
       b2 = np.array([[0, 0, 0], [1, -1, 1], [0, 0, 0]])

       b3: expect TIE (0)  > 500,000 boards explored; time around 20secs
       b3 = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

       b4: expect TIE(0) > 7,000,000 boards;  time around 4-5 mins
       b4 = np.array(
        [[1, 0, 0, 0], [0, 1, 0, -1], [0, -1, 1, 0], [0, 0, 0, -1]])
    '''

    print()
    print(f'board # - (score, board_count, time)')
    print()

    # Minimax for a board: evaluate the board
    #    expect win for X (1)  < 200 boards explored
    b1 = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])
    print(f"\n--------\nStart Board: \n{b1}")
    b1_score, b1_board_count, b1_time_elapsed = run_minimax(b1)
    print('b1 : expect win for X (1)  < 200 boards explored')
    print(f'b1: {b1_score, b1_board_count, b1_time_elapsed}')
    print()

    b2 = np.array([[0, 0, 0], [1, -1, 1], [0, 0, 0]])
    print(f"\n--------\nStart Board: \n{b2}")
    b2_score, b2_board_count, b2_time_elapsed = run_minimax(b2)
    print('b2:  expect win for O (-1)  > 1000 boards explored')
    print(f'b2: {b2_score, b2_board_count, b2_time_elapsed}')
    print()

    b3 = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    print(f"\n--------\nStart Board: \n{b3}")
    b3_score, b3_board_count, b3_time_elapsed = run_minimax(b3)
    print('b3: expect TIE (0)  > 500,000 boards explored; time around 20secs')
    print(f'b3:  {b3_score, b3_board_count, b3_time_elapsed}')
    print()

    b4 = np.array([[1, 0, 0, 0], [0, 1, 0, -1], [0, -1, 1, 0], [0, 0, 0, -1]])
    print(f"\n--------\nStart Board: \n{b4}")
    b4_score, b4_board_count, b4_time_elapsed = run_minimax(b4)
    print()
    print('b4: expect TIE(0) > 7,000,000 boards;  time around 4-5 mins')
    print(f'b4: {b4_score, b4_board_count, b4_time_elapsed}')


if __name__ == '__main__':
    run_code_tests()
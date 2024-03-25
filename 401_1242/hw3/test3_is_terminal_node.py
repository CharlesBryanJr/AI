import numpy as np

# test is_terminal_node
# tip: use your tested evaluate() to help with this

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

#### TEST CODE ##########
def run_tests():

    #TEST1 : Not terminal
    b = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])
    is_terminal = is_terminal_node(b)
    expected = False

    if is_terminal == expected:
        print (f"PASS Test 1 Non Terminal Board")
    else: print (f"FAIL Test 1 Non Terminal Board: \
        expect: {expected} actual: {is_terminal}")

    #TEST 2: Terminal
    b = np.array([[1, 1, 1], [1, -1, -1], [-1, 0, 0]])
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 2  Terminal Board")
    else:
        print(f"FAIL Test 2  Terminal Board: \
            expect: {expected} actual: {is_terminal}")


    #TEST3
    b = np.array([[1, -1, 1], [1, 1, -1], [-1, 1, -1]])
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 3  Terminal Board")
    else:
        print(f"FAIL Test 3  Terminal Board: \
            expect: {expected} actual: {is_terminal}")

    #TEST4 Win for X on diagonal
    b = np.array([[1, 0, 0], [0, 1, -1], [-1, -1, 1]])
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 4  Terminal Board")
    else:
        print(f"FAIL Test 4  Terminal Board: \
            expect: {expected} actual: {is_terminal}")

    #TEST5 win for O on reverse diagonal
    b = np.array([[1, 1, -1], [0, -1, 1], [-1, -1, 1]])
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 5  Terminal Board")
    else:
        print(f"FAIL Test 5  Terminal Board: \
            expect: {expected} actual: {is_terminal}")


    #TEST6 win for O on reverse diagonal for 4x4 board
    b = np.array([[1, 1, 0, -1], [0, 0, -1, 1],
                  [0, -1, 1, 0], [-1,0,0,0]])
    is_terminal = is_terminal_node(b)
    expected = True

    if is_terminal == expected:
        print(f"PASS Test 6  Terminal Board")
    else:
        print(f"FAIL Test 6  Terminal Board: \
                expect: {expected} actual: {is_terminal}")




run_tests()
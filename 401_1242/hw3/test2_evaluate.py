import numpy as np

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



#### TEST CODE ##########
def run_tests():
    b = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])

    #TEST1 : No winner
    b = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])
    score = evaluate(b)
    expect = 0

    if score == expect:
        print (f"PASS Test 1 No Win")
    else: print (f"FAIL Test 1 No Win: \
        expect: {expect} actual: {score}")

    #TEST 2: Win for X
    b = np.array([[1, 0, -1], [1, 0, 0], [1, 0, -1]])
    score = evaluate(b)
    expect = 1

    if score == expect:
        print (f"PASS Test 2  column win")
    else: print (f"FAIL Test 2: column win \
        expect: {expect} actual: {score}")

    #TEST3 Win for O
    b = np.array([[-1, -1, -1], [1, 0, 1], [1, 0, 1]])
    score = evaluate(b)
    expect = -1

    if score == expect:
        print (f"PASS Test 3  row win")
    else: print (f"FAIL Test 3: row win \
        expect: {expect} actual: {score}")


    #TEST4 Win for X on diagonal
    b = np.array([[-1, -1, 1], [1, 1, 1], [1, 0, -1]])
    score = evaluate(b)
    expect = 1

    if score == expect:
        print (f"PASS Test 4  diag win")
    else: print (f"FAIL Test 4: diag win \
        expect: {expect} actual: {score}")

    #TEST5 win for O on reverse diagonal
    b = np.array([[-1, 1, 1], [1, -1, -1], [1, 0, -1]])
    score = evaluate(b)
    expect = -1

    if score == expect:
        print (f"PASS Test 5  diag2 win")
    else: print (f"FAIL Test 5: diag2 win \
        expect: {expect} actual: {score}")

    #TEST6 win for O on reverse diagonal for 4x4 board
    b = np.array([[-1, 1, 1, 0], [1, -1, -1, 0], \
                  [1, 0, -1, 0], [1,0,0,-1]])
    score = evaluate(b)
    expect = -1

    if score == expect:
        print (f"PASS Test 6  diag2 win 4x4")
    else: print (f"FAIL Test 6: diag2 win 4x4 \
        expect: {expect} actual: {score}")


run_tests()
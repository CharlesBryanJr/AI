# test get_child_boards - separate test file
import numpy as np

def getChildren(board, char):
    ''' numpy version '''
    if not char in ['X', 'O']:
        raise ValueError("get_child_boards: expecting char='X' or 'O' ")

    newval = -1
    if char == 'X': newval = 1

    child_list = get_child_boards(board, char)
    return child_list


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


def get_max_number_child_boards(board):
    zero_count = 0
    for i in board:
        for j in i:
            if j == 0:
                zero_count +=1
    return zero_count



def run_tests():
    b = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])

    #TEST1 length of child list
    expect = b.size - np.count_nonzero(b)
    child_list = getChildren(b, 'X')

    if len(child_list) == expect:
        print (f"PASS Test 1")
    else: print (f"FAIL Test 1: \
        expect: {expect} actual: {len(child_list)}")

    #TEST2 - is expected board in list
    b2 = np.array([[1, 1, -1], [1, 0, 0], [-1, 0, 0]])
    found = False
    for board in child_list:
        if np.array_equal(board, b2):
            found = True
            break

    if found:
        print ("PASS Test 2")
    else: print (f"FAIL Test 2: Expected board not in child list")

    #TEST3 Test 4x4 array
    b3 = np.array([ [0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0] ])
    expect = b3.size - np.count_nonzero(b3)
    child_list = getChildren(b3, 'X')

    if len(child_list) == expect:
        print(f"PASS Test 3  4x4 array")
    else:
        print(f"FAIL Test 3 4x4 array: \
            expect: {expect} actual: {len(child_list)}")

run_tests()

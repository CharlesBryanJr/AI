import numpy as np


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




def get_child_boards2(board, char):
    child_boards = []
    fill_value = 1 if char == 'X' else -1

    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i][j] == 0:
                new_board = np.copy(board)
                new_board[i][j] = fill_value
                child_boards.append(new_board)

    return child_boards


b1 = np.array([[1, 0, -1], [1, 0, 0], [-1, 0, 0]])

# Generate child boards for the start state
child_boards = get_child_boards(b1, 'X')
child_boards2 = get_child_boards2(b1, 'X')

print(b1)
print()
print(f'child_boards - {child_boards}')



'''
def get_child_boards(board, char):
    player = 1 if char == 'X' else -1
    child_boards = []

    child_board = []
    found_new_move = False
    for i in range(len(board)):
        row = []
        for j in range(len(board[i])):
            curr = board[i][j]
            if found_new_move:
                row.append(curr)
            elif curr in (-1, 1):
                row.append(curr)
            else:
                row.append(player)
                found_new_move = True
        child_board.append(row)

    child_boards.append(np.array(child_board))
    return child_boards
'''
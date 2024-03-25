def minimax(node, depth, maximizingPlayer):
    if depth == 0 or is_terminal(node):
        return static_evaluation(node)

    if maximizingPlayer:
        maxEva = float('-inf')
        for child in children(node):
            eva = minimax(child, depth - 1, False)
            maxEva = max(maxEva, eva)
        return maxEva
    else:
        minEva = float('inf')
        for child in children(node):
            eva = minimax(child, depth - 1, True)
            minEva = min(minEva, eva)
        return minEva


def is_terminal(board):
    """ Check if the game board is a terminal state (win, lose, draw). """
    winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                         (0, 4, 8), (2, 4, 6)]  # Diagonals
    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != None:
            return True
    return all(cell is not None for cell in board)


def static_evaluation(board):
    """ Evaluate the board for a win/lose/draw situation. """
    if check_win(board, 'X'):
        return 10
    elif check_win(board, 'O'):
        return -10
    else:
        return 0


def check_win(board, player):
    """ Check if a player has won the game. """
    winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6)]
    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False


def children(board, player):
    """ Generate all possible successor boards (children) for the given player. """
    children_boards = []
    for i, cell in enumerate(board):
        if cell is None:
            new_board = board.copy()
            new_board[i] = player
            children_boards.append(new_board)
    return children_boards


def minimax(board, depth, maximizingPlayer):
    if depth == 0 or is_terminal(board):
        return static_evaluation(board)

    if maximizingPlayer:  # If it's X's turn
        maxEva = float('-inf')
        for child in children(board, 'X'):
            eva = minimax(child, depth - 1, False)
            maxEva = max(maxEva, eva)
        return maxEva
    else:  # If it's O's turn
        minEva = float('inf')
        for child in children(board, 'O'):
            eva = minimax(child, depth - 1, True)
            minEva = min(minEva, eva)
        return minEva


# Start with an empty board
initial_board = [None] * 9
# Call minimax with the initial board, starting depth, and True assuming 'X' starts the game
best_move_score = minimax(initial_board, depth=9, maximizingPlayer=True)
print(f'best_move_score: {best_move_score}')

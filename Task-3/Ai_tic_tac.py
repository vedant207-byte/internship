import math

HUMAN = 'O'
AI = 'X'
EMPTY = ' '

def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board, player):
    win_states = (
        [board[i] for i in range(3)] +
        [[board[i][j] for i in range(3)] for j in range(3)] +
        [[board[i][i] for i in range(3)]] +
        [[board[i][2 - i] for i in range(3)]]
    )
    return [player] * 3 in win_states

def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):
        return 10 - depth
    if check_winner(board, HUMAN):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best = min(best, score)
        return best

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O'. AI is 'X'.")
    print_board(board)

    while True:
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == EMPTY:
                    board[row][col] = HUMAN
                    break
                else:
                    print("Cell is already taken!")
            except:
                print("Invalid input. Try again.")
        
        print_board(board)
        if check_winner(board, HUMAN):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        print("AI is thinking...")
        row, col = best_move(board)
        board[row][col] = AI
        print_board(board)

        if check_winner(board, AI):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()

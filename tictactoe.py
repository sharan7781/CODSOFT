import tkinter as tk
import tkinter.messagebox

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Minimax function
def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):
        return -1
    if check_win(board, "O"):
        return 1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ""
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ""
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to make AI's move using Minimax
def make_ai_move(board):
    best_eval = float("-inf")
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                eval = minimax(board, 0, False)
                board[i][j] = ""
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    return best_move

# Function to handle player's move
def player_move(row, col):
    if board[row][col] == "" and not game_over:
        board[row][col] = "X"
        buttons[row][col].config(text="X", state=tk.DISABLED)
        if check_win(board, "X"):
            end_game("Player X wins!")
        elif is_full(board):
            end_game("It's a draw!")
        else:
            ai_row, ai_col = make_ai_move(board)
            board[ai_row][ai_col] = "O"
            buttons[ai_row][ai_col].config(text="O", state=tk.DISABLED)
            if check_win(board, "O"):
                end_game("AI wins!")

# Function to handle game end
def end_game(message):
    global game_over
    game_over = True
    tk.messagebox.showinfo("Game Over", message)

# Function to check if the board is full
def is_full(board):
    return all(all(cell != "" for cell in row) for row in board)

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

board = [["" for _ in range(3)] for _ in range(3)]
buttons = []

# Create the buttons
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, text="", font=("Helvetica", 24), width=5, height=2, command=lambda i=i, j=j: player_move(i, j))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

game_over = False

# Start the main loop
root.mainloop()

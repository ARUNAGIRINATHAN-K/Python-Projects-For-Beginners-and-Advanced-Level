import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Global variables
current_player = 'X'
board = [' ' for _ in range(9)]

# Function to handle button click
def button_click(index):
    global current_player
    if board[index] == ' ':
        board[index] = current_player
        buttons[index].config(text=current_player)
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif ' ' not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Function to check for a winner
def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                            (0, 4, 8), (2, 4, 6)]  # Diagonals
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return False

# Function to reset the game
def reset_game():
    global board, current_player
    board = [' ' for _ in range(9)]
    current_player = 'X'
    for button in buttons:
        button.config(text=' ')

# Create buttons for the grid
buttons = []
for i in range(9):
    button = tk.Button(root, text=' ', width=10, height=3, font=("Arial", 20),
                       command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Start the Tkinter main loop
root.mainloop()

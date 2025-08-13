import tkinter as tk
from tkinter import messagebox, ttk
from sudoku_generator import generate_puzzle
from sudoku_solver import solve_sudoku

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")

        self.entries = []
        self.difficulty = tk.StringVar(value="Medium")
        self.puzzle = []
        self.solution = []

        # Difficulty Dropdown
        ttk.Label(root, text="Difficulty:").grid(row=0, column=0, columnspan=2, sticky="w")
        self.difficulty_menu = ttk.Combobox(root, textvariable=self.difficulty, values=["Easy", "Medium", "Hard"], state="readonly", width=10)
        self.difficulty_menu.grid(row=0, column=2, columnspan=2, pady=5)

        # New Puzzle Button
        tk.Button(root, text="New Puzzle", command=self.load_new_puzzle).grid(row=0, column=4, columnspan=2, pady=5)

        self.create_grid()
        self.load_new_puzzle()

        # Action Buttons
        tk.Button(root, text="Check Solution", command=self.check_solution).grid(row=10, column=0, columnspan=4, pady=10)
        tk.Button(root, text="Solve Puzzle", command=self.solve_puzzle).grid(row=10, column=5, columnspan=4, pady=10)

    def create_grid(self):
        for i in range(9):
            row = []
            for j in range(9):
                e = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center')
                e.grid(row=i+1, column=j, padx=1, pady=1)
                row.append(e)
            self.entries.append(row)

    def load_new_puzzle(self):
        diff = self.difficulty.get()
        if diff == "Easy":
            remove = 30
        elif diff == "Medium":
            remove = 40
        else:  # Hard
            remove = 50

        self.puzzle, self.solution = generate_puzzle(removal_count=remove)

        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].config(state='normal', fg='black')
                if self.puzzle[i][j] != 0:
                    self.entries[i][j].insert(0, str(self.puzzle[i][j]))
                    self.entries[i][j].config(state='disabled', disabledforeground='black')

    def get_grid(self):
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                row.append(int(val) if val.isdigit() else 0)
            grid.append(row)
        return grid

    def check_solution(self):
        grid = self.get_grid()

        def is_valid_block(block):
            return sorted(block) == list(range(1, 10))

        for row in grid:
            if not is_valid_block(row):
                messagebox.showerror("Error", "Invalid row.")
                return

        for col in zip(*grid):
            if not is_valid_block(col):
                messagebox.showerror("Error", "Invalid column.")
                return

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                block = [grid[r][c] for r in range(box_row, box_row+3) for c in range(box_col, box_col+3)]
                if not is_valid_block(block):
                    messagebox.showerror("Error", "Invalid block.")
                    return

        messagebox.showinfo("Success", "Congratulations! Sudoku solved correctly.")

    def solve_puzzle(self):
        grid = self.get_grid()
        if solve_sudoku(grid):
            for i in range(9):
                for j in range(9):
                    if self.puzzle[i][j] == 0:
                        self.entries[i][j].delete(0, tk.END)
                        self.entries[i][j].insert(0, str(grid[i][j]))
                        self.entries[i][j].config(fg='blue')
        else:
            messagebox.showerror("No Solution", "Could not solve this puzzle.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()

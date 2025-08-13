import tkinter as tk
from tkinter import ttk

class NQueensGUI:
    def __init__(self, master):
        self.master = master
        self.n = 8  # default board size
        self.solutions = []
        self.current = 0

        # N selection label and dropdown
        self.n_label = tk.Label(master, text="Select N:")
        self.n_label.pack()

        self.n_var = tk.IntVar(value=self.n)
        self.dropdown = ttk.Combobox(master, textvariable=self.n_var, values=list(range(4, 11)))
        self.dropdown.pack()

        # Solve button
        self.solve_button = tk.Button(master, text="Solve", command=self.generate_solutions)
        self.solve_button.pack(pady=5)

        # Canvas to draw board
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack(pady=10)

        # Navigation buttons
        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        self.prev_button = tk.Button(self.button_frame, text="<< Prev", command=self.show_prev)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(self.button_frame, text="Next >>", command=self.show_next)
        self.next_button.pack(side=tk.RIGHT, padx=10)

        # Status label for solution count
        self.status_label = tk.Label(master, text="Select N and click Solve")
        self.status_label.pack(pady=5)

    def generate_solutions(self):
        self.n = self.n_var.get()
        self.solutions = self.solve_n_queens(self.n)
        self.current = 0
        total = len(self.solutions)
        if total > 0:
            self.status_label.config(text=f"Showing solution 1 of {total}")
        else:
            self.status_label.config(text="No solutions found.")
        self.draw_board()

    def solve_n_queens(self, n):
        def is_safe(board, row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i][j] == 'Q':
                    return False
            return True

        def solve(board, row):
            if row == n:
                solutions.append(["".join(r) for r in board])
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    solve(board, row + 1)
                    board[row][col] = '.'

        board = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []
        solve(board, 0)
        return solutions

    def draw_board(self):
        self.canvas.delete("all")
        if not self.solutions:
            return

        cell_size = 500 // self.n
        solution = self.solutions[self.current]

        for i in range(self.n):
            for j in range(self.n):
                x1 = j * cell_size
                y1 = i * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                fill = "white" if (i + j) % 2 == 0 else "gray"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill)
                if solution[i][j] == 'Q':
                    self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2,
                                            text='♕', font=("Arial", cell_size // 2), fill="red")

    def show_next(self):
        if self.solutions:
            self.current = (self.current + 1) % len(self.solutions)
            self.status_label.config(text=f"Showing solution {self.current + 1} of {len(self.solutions)}")
            self.draw_board()

    def show_prev(self):
        if self.solutions:
            self.current = (self.current - 1) % len(self.solutions)
            self.status_label.config(text=f"Showing solution {self.current + 1} of {len(self.solutions)}")
            self.draw_board()


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.title("N-Queens Visualizer")
    NQueensGUI(root)
    root.mainloop()

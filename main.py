import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Крестики-нолики")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=("Helvetica", 20), width=6, height=3,
                                                command=lambda i=i, j=j: self.click_button(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def click_button(self, row, col):
        if self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.current_player
            self.board[row][col] = self.current_player

            if self.check_winner(row, col):
                messagebox.showinfo("Победа!", f"Игрок {self.current_player} победил!")
                self.reset_board()
                return

            if self.check_draw():
                messagebox.showinfo("Ничья", "Ничья!")
                self.reset_board()
                return

            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, row, col):
        # Проверка по строкам и столбцам
        if all(self.board[row][c] == self.current_player for c in range(3)) or \
           all(self.board[r][col] == self.current_player for r in range(3)):
            return True

        # Проверка по диагоналям
        if row == col and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        if row + col == 2 and all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True

        return False

    def check_draw(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.board[i][j] = ""
        self.current_player = "X"

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()

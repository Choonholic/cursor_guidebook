import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []

        # Create buttons for the game board
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.window,
                    text="",
                    font=('Arial', 20),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def button_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(
                text=self.current_player,
                fg="red" if self.current_player == "X" else "blue"
            )

            # Check for winner
            winner = self.check_winner()
            if winner:
                # Ask if the player wants to start a new game
                if messagebox.askyesno("Game Over", f"Player {winner} wins! Do you want to start a new game?"):
                    self.reset_game()  # 새로운 게임 시작
                else:
                    self.window.destroy()  # 게임 종료
                return

            # Check for tie
            if self.is_board_full():
                if messagebox.askyesno("Game Over", "It's a tie! Do you want to start a new game?"):
                    self.reset_game()  # 새로운 게임 시작
                else:
                    self.window.destroy()  # 게임 종료
                return

            # Switch player
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return self.board[i]

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return self.board[i]

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]

        return None

    def is_board_full(self):
        return " " not in self.board

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()

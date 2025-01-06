def print_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")

def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]

    return None

def is_board_full(board):
    return " " not in board

def main():
    board = [" " for _ in range(9)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered from 1-9, left to right, top to bottom.")

    while True:
        print_board(board)

        # Get player move
        while True:
            try:
                position = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
                if 0 <= position <= 8 and board[position] == " ":
                    break
                print("Invalid position. Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

        # Make move
        board[position] = current_player

        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()

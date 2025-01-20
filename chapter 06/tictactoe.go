package main

import (
	"fmt"
)

type TicTacToe struct {
	board         [9]string
	currentPlayer string
}

func NewTicTacToe() *TicTacToe {
	return &TicTacToe{
		board:         [9]string{" ", " ", " ", " ", " ", " ", " ", " ", " "},
		currentPlayer: "X",
	}
}

func (t *TicTacToe) printBoard() {
	for i := 0; i < 9; i += 3 {
		fmt.Printf("%s | %s | %s\n", t.board[i], t.board[i+1], t.board[i+2])
		if i < 6 {
			fmt.Println("--+---+--")
		}
	}
}

func (t *TicTacToe) makeMove(position int) bool {
	if position < 0 || position >= 9 || t.board[position] != " " {
		return false
	}
	t.board[position] = t.currentPlayer
	return true
}

func (t *TicTacToe) checkWinner() string {
	// Check rows, columns, and diagonals
	winPatterns := [][3]int{
		{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, // rows
		{0, 3, 6}, {1, 4, 7}, {2, 5, 8}, // columns
		{0, 4, 8}, {2, 4, 6},            // diagonals
	}

	for _, pattern := range winPatterns {
		if t.board[pattern[0]] == t.board[pattern[1]] && t.board[pattern[1]] == t.board[pattern[2]] && t.board[pattern[0]] != " " {
			return t.board[pattern[0]]
		}
	}
	return ""
}

func (t *TicTacToe) isBoardFull() bool {
	for _, cell := range t.board {
		if cell == " " {
			return false
		}
	}
	return true
}

func (t *TicTacToe) switchPlayer() {
	if t.currentPlayer == "X" {
		t.currentPlayer = "O"
	} else {
		t.currentPlayer = "X"
	}
}

func (t *TicTacToe) run() {
	for {
		t.printBoard()
		var position int
		fmt.Printf("Player %s, enter your move (0-8): ", t.currentPlayer)
		fmt.Scan(&position)

		if !t.makeMove(position) {
			fmt.Println("Invalid move, try again.")
			continue
		}

		winner := t.checkWinner()
		if winner != "" {
			t.printBoard()
			fmt.Printf("Player %s wins!\n", winner)
			break
		}

		if t.isBoardFull() {
			t.printBoard()
			fmt.Println("It's a tie!")
			break
		}

		t.switchPlayer()
	}
}

func main() {
	game := NewTicTacToe()
	game.run()
}

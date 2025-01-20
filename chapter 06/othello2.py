import pygame
import sys
import numpy as np
from tkinter import messagebox, Tk

# Constants
BOARD_SIZE = 8
TILE_SIZE = 80
WINDOW_SIZE = BOARD_SIZE * TILE_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)

# Initialize PyGame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Othello')

# Initialize board
board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
board[3][3] = board[4][4] = 1  # White
board[3][4] = board[4][3] = -1  # Black

current_player = 1  # 1 for White, -1 for Black

def draw_board():
    screen.fill(GREEN)
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)
            if board[y][x] == 1:
                pygame.draw.circle(screen, WHITE, rect.center, TILE_SIZE // 2 - 5)
            elif board[y][x] == -1:
                pygame.draw.circle(screen, BLACK, rect.center, TILE_SIZE // 2 - 5)

def is_valid_move(x, y, player):
    if board[y][x] != 0:
        return False
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == -player:
            while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                nx += dx
                ny += dy
                if not (0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE):
                    break
                if board[ny][nx] == 0:
                    break
                if board[ny][nx] == player:
                    return True
    return False

def make_move(x, y, player):
    board[y][x] = player
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == -player:
            path = []
            while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                if board[ny][nx] == 0:
                    break
                if board[ny][nx] == player:
                    for px, py in path:
                        board[py][px] = player
                    break
                path.append((nx, ny))
                nx += dx
                ny += dy

def has_valid_moves(player):
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if is_valid_move(x, y, player):
                return True
    return False

def check_winner():
    white_count = np.sum(board == 1)
    black_count = np.sum(board == -1)
    if white_count > black_count:
        return "White wins!"
    elif black_count > white_count:
        return "Black wins!"
    else:
        return "It's a tie!"

def main():
    global current_player
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x //= TILE_SIZE
                y //= TILE_SIZE
                if is_valid_move(x, y, current_player):
                    make_move(x, y, current_player)
                    current_player = -current_player if has_valid_moves(-current_player) else current_player

        draw_board()
        pygame.display.flip()

        if not has_valid_moves(1) and not has_valid_moves(-1):
            Tk().wm_withdraw()  # to hide the main window
            result = messagebox.askyesno("Game Over", f"{check_winner()} Do you want to play again?")
            if result:
                board.fill(0)
                board[3][3] = board[4][4] = 1
                board[3][4] = board[4][3] = -1
                current_player = 1
            else:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()

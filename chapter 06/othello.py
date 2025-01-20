import pygame
import sys
import numpy as np

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

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()

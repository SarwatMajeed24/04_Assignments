import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600  # Canvas dimensions
CELL_SIZE = 20  # Size of each cell
ERASER_SIZE = 40  # Size of the eraser
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
ERASER_COLOR = (255, 0, 0)  # Red color for the eraser

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canvas with Eraser")

# Create the grid (2D array of cells, all initially blue)
grid = [[BLUE for _ in range(COLS)] for _ in range(ROWS)]

# Eraser rectangle position
eraser_x, eraser_y = 100, 100  # Starting position of the eraser
eraser_rect = pygame.Rect(eraser_x, eraser_y, ERASER_SIZE, ERASER_SIZE)

# Game loop
running = True
dragging = False  # Whether the eraser is being dragged

while running:
    screen.fill(WHITE)  # Fill the screen with white background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if eraser_rect.collidepoint(event.pos):
                dragging = True
        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        if event.type == pygame.MOUSEMOTION and dragging:
            eraser_rect.x, eraser_rect.y = event.pos

    # Erase the cells under the eraser
    eraser_left = eraser_rect.left // CELL_SIZE
    eraser_right = (eraser_rect.right // CELL_SIZE)
    eraser_top = eraser_rect.top // CELL_SIZE
    eraser_bottom = eraser_rect.bottom // CELL_SIZE

    for row in range(eraser_top, eraser_bottom):
        for col in range(eraser_left, eraser_right):
            if 0 <= row < ROWS and 0 <= col < COLS:
                grid[row][col] = WHITE  # Set cell color to white (erased)

    # Draw the grid
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, grid[row][col], (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw the eraser rectangle (red for visibility)
    pygame.draw.rect(screen, ERASER_COLOR, eraser_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()


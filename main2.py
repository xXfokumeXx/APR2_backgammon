import pygame

# Define the dimensions of the table
TABLE_WIDTH = 600
TABLE_HEIGHT = 400

# Initialize Pygame
pygame.init()

# Create the table surface
table_surface = pygame.display.set_mode((TABLE_WIDTH, TABLE_HEIGHT))
pygame.display.set_caption("Backgammon Table")

# Set the background color
background_color = (222, 184, 135)  # Burlywood
table_surface.fill(background_color)

# Define the board colors
board_color1 = (139, 69, 19)  # Saddlebrown
board_color2 = (244, 164, 96)  # Sandybrown

# Define the dimensions of the board
board_width = TABLE_WIDTH - 100
board_height = TABLE_HEIGHT - 100

# Define the number of columns and rows on the board
num_columns = 12
num_rows = 2

# Calculate the width and height of each cell
cell_width = board_width // num_columns
cell_height = board_height // num_rows

# Draw the board
for row in range(num_rows):
    for col in range(num_columns):
        x = 50 + col * cell_width
        y = 50 + row * cell_height
        if row % 2 == 0:
            color = board_color1 if col % 2 == 0 else board_color2
        else:
            color = board_color2 if col % 2 == 0 else board_color1
        pygame.draw.rect(table_surface, color, pygame.Rect(x, y, cell_width, cell_height))

# Update the table display
pygame.display.flip()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit the game
pygame.quit()
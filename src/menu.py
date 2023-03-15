import pygame
import sys
from arena import Arena

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Set the font
font = pygame.font.SysFont(None, 30)
start_button = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25, 100, 50)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

arena=Arena()

# Define the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle key presses
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                arena.run()

    # Draw the background
    screen.fill(WHITE)

    # Draw the title
    title_text = font.render("My Game", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))

    # Draw the instructions
    instructions_text = font.render("Start", True, BLACK)
    screen.blit(instructions_text, (start_button.centerx - instructions_text.get_width() // 2, start_button.centery - instructions_text.get_height() // 2))

    # Draw the start button
    pygame.draw.rect(screen, BLACK, start_button, 2)

    # Update the display
    pygame.display.update()

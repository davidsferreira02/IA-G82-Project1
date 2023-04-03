import pygame
import sys
from sizeMenu import SizeMenu
from instructions import Instructions

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (44, 119, 242)  # a blue color for the background
GREEN = (148, 252, 96)  # a green color for the buttons
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Set the font
font = pygame.font.Font("PressStart2P-Regular.ttf", 15)  # use a custom font
start_button = pygame.Rect(SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 - 25, 200, 50)  # adjust the button positions
instructions_button = pygame.Rect(SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 + 50, 200, 50)
quit_button = pygame.Rect(SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 + 125, 200, 50)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

sizeMenu = SizeMenu()
instructions = Instructions()

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
                sizeMenu.run()

            if instructions_button.collidepoint(event.pos):
                instructions.run()

            if quit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    # Draw the background
    screen.fill(BLUE)
    

    # Draw the title
    title_text = font.render("Space Block - Roll the Block", True,WHITE)
    screen.blit(title_text, (((SCREEN_WIDTH // 2) + 80) - title_text.get_width() // 2, 50))

    # Draw the buttons
    pygame.draw.rect(screen,BLACK, start_button)
    start_text = font.render("Start", True, WHITE)
    screen.blit(start_text, (start_button.centerx - start_text.get_width() // 2, start_button.centery - start_text.get_height() // 2))

    pygame.draw.rect(screen, BLACK, instructions_button)
    instructions_text = font.render("Instructions", True, WHITE)
    screen.blit(instructions_text, (instructions_button.centerx - instructions_text.get_width() // 2, instructions_button.centery - instructions_text.get_height() // 2))

    pygame.draw.rect(screen, BLACK, quit_button)
    quit_text = font.render("Quit", True, WHITE)
    screen.blit(quit_text, (quit_button.centerx - quit_text.get_width() // 2, quit_button.centery - quit_text.get_height() // 2))

    # Add some animations
    if start_button.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (255, 255, 255), start_button, 2)
    if instructions_button.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (255, 255, 255), instructions_button, 2)
    if quit_button.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (255,255,255),quit_button,2)


    # Update the display
    pygame.display.update()

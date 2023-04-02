import pygame
import sys
from arena import Arena
from instructions import Instructions

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Set the font
font = pygame.font.SysFont(None, 30)
start_button = pygame.Rect(SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2 - 25, 150, 50)
instructions_button = pygame.Rect(SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2 + 50 , 150, 50)
quit_button=pygame.Rect(SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2 + 120, 150, 50)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

arena = Arena()
instructions=Instructions()

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

            if instructions_button.collidepoint(event.pos):
                instructions.run()
            
            if quit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()   
    

    # Draw the background
    screen.fill(WHITE)

    # Draw the title
    title_text = font.render(" Space Block – Roll the Block ", True, BLACK)
    screen.blit(title_text, (((SCREEN_WIDTH // 2 )+80) - title_text.get_width() // 2, 100))

    # Draw the instructions
    start_text = font.render("Start", True, BLACK)
    screen.blit(start_text, (start_button.centerx - start_text.get_width() // 2, start_button.centery - start_text.get_height() // 2))

    instructions_text = font.render("Instructions", True, BLACK)
    screen.blit(instructions_text, (instructions_button.centerx - instructions_text.get_width() // 2, instructions_button.centery - instructions_text.get_height() // 2))

    quit_text = font.render("Quit", True, BLACK)
    screen.blit(quit_text, (quit_button.centerx - quit_text.get_width() // 2, quit_button.centery - quit_text.get_height() // 2))


   

    # Draw the start button
    pygame.draw.rect(screen, BLACK, start_button, 2)
    pygame.draw.rect(screen,BLACK,instructions_button,2)
    pygame.draw.rect(screen,BLACK,quit_button,2)

    # Update the display
    pygame.display.update()

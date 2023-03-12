'''import pygame
from player import Player
ARENA_WIDTH = 30
ARENA_HEIGHT = 50
BLOCK_SIZE = 30  


pygame.init()


screen = pygame.display.set_mode((ARENA_WIDTH * BLOCK_SIZE, ARENA_HEIGHT * BLOCK_SIZE))
player1=Player("David")

# Define colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
player_name = player1.get_name()
score = 0
font = pygame.font.SysFont(None, 30)

# Draw the background
screen.fill(GRAY)


for i in range(ARENA_WIDTH + 1):
    pygame.draw.line(screen, BLACK, (i * BLOCK_SIZE, 0), (i * BLOCK_SIZE, ARENA_HEIGHT * BLOCK_SIZE))
for j in range(ARENA_HEIGHT + 1):
    pygame.draw.line(screen, BLACK, (0, j * BLOCK_SIZE), (ARENA_WIDTH * BLOCK_SIZE, j * BLOCK_SIZE))


name_text = font.render(f"Player: {player_name}", True, WHITE)
score_text = font.render(f"Score: {score}", True, WHITE)

# Blit the text onto the screen
screen.blit(name_text, (ARENA_WIDTH * BLOCK_SIZE - name_text.get_width() - 10, 10))
screen.blit(score_text, (ARENA_WIDTH * BLOCK_SIZE - score_text.get_width() - 10, 40))
# Update the display
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            '''
import pygame
from player import Player

ARENA_WIDTH = 20
ARENA_HEIGHT = 15
BLOCK_WIDTH =50
BLOCK_HEIGHT=50
BLOCK_SIZE=40 

# Define colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((ARENA_WIDTH * BLOCK_SIZE, ARENA_HEIGHT * BLOCK_SIZE))

# Create the player
player = Player("David", 0, 0)

# Set the clock
clock = pygame.time.Clock()

# Set the font
font = pygame.font.SysFont(None, 30)

# Define the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
            elif event.key == pygame.K_UP:
                player.move_up()
            elif event.key == pygame.K_DOWN:
                player.move_down()

    # Draw the background
    screen.fill(GRAY)

    # Draw the grid
    for i in range(ARENA_WIDTH):
        for j in range(ARENA_HEIGHT):
            rect = pygame.Rect(i * BLOCK_SIZE, j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

    # Draw the player
    player_rect = pygame.Rect(player.x * BLOCK_SIZE, player.y * BLOCK_SIZE, BLOCK_WIDTH, BLOCK_HEIGHT)
    pygame.draw.rect(screen, RED, player_rect)

    # Draw the score
    score_text = font.render(f"Score: {player.score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    level_text = font.render(f"Level: {player.level}", True, WHITE)
    screen.blit(level_text, (10, 30))
    


    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(10)
           
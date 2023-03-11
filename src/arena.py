import pygame

ARENA_WIDTH = 30
ARENA_HEIGHT = 50
BLOCK_SIZE = 30  


pygame.init()


screen = pygame.display.set_mode((ARENA_WIDTH * BLOCK_SIZE, ARENA_HEIGHT * BLOCK_SIZE))

# Define colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
player_name = "Player 1"
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
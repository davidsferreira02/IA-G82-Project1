import random
import pygame
import sys
from player import Player


class Arena:


 ARENA_WIDTH = 20
 ARENA_HEIGHT = 15
 BLOCK_WIDTH = 50
 BLOCK_HEIGHT = 70
 BLOCK_SIZE = 40

# Define colors
 BLACK = (0, 0, 0)
 GRAY = (128, 128, 128)
 WHITE = (255, 255, 255)
 RED = (255, 0, 0)
 GOLD = (255, 215, 0)

# Initialize Pygame
 pygame.init()

# Create the screen
 screen = pygame.display.set_mode(
    (ARENA_WIDTH * BLOCK_SIZE, ARENA_HEIGHT * BLOCK_SIZE))

# Create the player
 player = Player("David", 0, 0)



# Set the clock
 clock = pygame.time.Clock()

# Set the font
 font = pygame.font.SysFont(None, 30)


 black_blocks = []
 for i in range(random.randint(1, 30)):
    x = random.randint(0, ARENA_WIDTH-1)
    y = random.randint(0, ARENA_HEIGHT-1)
    black_blocks.append((x, y))
    
 golden_block = (random.randint(0, ARENA_WIDTH-1),
                random.randint(0, ARENA_HEIGHT-1))

 golden_block_X=golden_block[0]
 golden_block_Y=golden_block[1] 

 score_level=0             

# Define the game loop
 while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if(player.x==golden_block_X and player.y==golden_block_Y): 
            player.update_score()   

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
        if player.score>player.level:

            player.update_level()
            black_blocks = []
            for i in range(random.randint(1, 30)):
             x = random.randint(0, ARENA_WIDTH-1)
             y = random.randint(0, ARENA_HEIGHT-1)
             black_blocks.append((x, y))
             golden_block = (random.randint(0, ARENA_WIDTH-1),
             random.randint(0, ARENA_HEIGHT-1))
             golden_block_X=golden_block[0]
             golden_block_Y=golden_block[1]  


    # Draw the background
    screen.fill(GRAY)

    for block in black_blocks:
        block_rect = pygame.Rect(
            block[0] * BLOCK_SIZE, block[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, BLACK, block_rect)

    
    golden_rect = pygame.Rect(
        golden_block[0] * BLOCK_SIZE, golden_block[1] * BLOCK_SIZE, BLOCK_WIDTH,  BLOCK_HEIGHT)
    pygame.draw.rect(screen, GOLD, golden_rect)
    


   

    # Draw the grid
    for i in range(ARENA_WIDTH):
        for j in range(ARENA_HEIGHT):
            rect = pygame.Rect(i * BLOCK_SIZE, j *
                               BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

    # Draw the player
    player_rect = pygame.Rect(player.x * BLOCK_SIZE,
                              player.y * BLOCK_SIZE, BLOCK_WIDTH, BLOCK_HEIGHT)
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

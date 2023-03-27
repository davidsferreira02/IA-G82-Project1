
import pygame
import sys
import random
from player import Player

class Instructions:
    ARENA_WIDTH = 20
    ARENA_HEIGHT = 15
    BLOCK_WIDTH = 45
    BLOCK_HEIGHT = 60
    BLOCK_SIZE = 40
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480

    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GOLD = (255, 215, 0)
    
    
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.font = pygame.font.SysFont(None, 30)
        self.player = Player("Player", 0, 0, 'UP')
        self.clock = pygame.time.Clock()
        # Create the screen
        self.screen = pygame.display.set_mode(
            (self.ARENA_WIDTH * self.BLOCK_SIZE, self.ARENA_HEIGHT * self.BLOCK_SIZE))



    def run(self):
         # Define the game loop
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    

                

            # Draw the background
            self.screen.fill(self.WHITE)

            title_text = self.font.render(" How to play ", True, self.BLACK)
            self.screen.blit(title_text, (((self.SCREEN_WIDTH // 2 )+80) - title_text.get_width() // 2, 100))

    # Update the display
            pygame.display.update()

    # Set the frame rate
            self.clock.tick(10)

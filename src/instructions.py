
import pygame
import sys
import random
from player import Player

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
BLUE = (44, 119, 242)

class Instructions:
   
    
    
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.font = pygame.font.Font("PressStart2P-Regular.ttf", 15)
        self.font1 = pygame.font.Font("PressStart2P-Regular.ttf", 11)
        self.clock = pygame.time.Clock()
        # Create the screen
        self.screen = pygame.display.set_mode(
            (ARENA_WIDTH * BLOCK_SIZE, ARENA_HEIGHT * BLOCK_SIZE))



    def run(self):
         # Define the game loop
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    

                

            # Draw the background
            self.screen.fill(BLUE)

            title_text = self.font.render(" How to play ", True, WHITE)
            self.screen.blit(title_text, (((SCREEN_WIDTH // 2 )+80) - title_text.get_width() // 2, 100))


            instructions_text1 = self.font.render("The goal on our game is to reach to golden block ", True, BLACK)
            self.screen.blit(instructions_text1, (((SCREEN_WIDTH // 2 )+200) - (instructions_text1.get_width() // 2) -150, 150))

            instructions_text2 = self.font.render("On minimal plays possivel  ", True, BLACK)
            self.screen.blit(instructions_text2, (((SCREEN_WIDTH // 2 )+200) - (instructions_text2.get_width() // 2) -150, 200))

            instructions_text3 = self.font.render("If you touch the black block you lose  ", True, BLACK)
            self.screen.blit(instructions_text3, (((SCREEN_WIDTH // 2 )+200) - (instructions_text3.get_width() // 2) -150, 250))
            instructions_text4 = self.font.render("You can move the block with arroys keys ", True, BLACK)
            self.screen.blit(instructions_text4, (((SCREEN_WIDTH // 2 )+200) - (instructions_text4.get_width() // 2) -150, 300))
            instructions_text5 = self.font1.render("The player block only reach the golden block if their status==UP ", True, BLACK)
            self.screen.blit(instructions_text5, (((SCREEN_WIDTH // 2 )+200) - (instructions_text5.get_width() // 2) -150, 350))


            


    # Update the display
            pygame.display.update()

    # Set the frame rate
            self.clock.tick(10)

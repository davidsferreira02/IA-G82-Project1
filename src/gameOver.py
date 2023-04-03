import pygame
import sys
from player import Player


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (44, 119, 242)  # a blue color for the background
GREEN = (148, 252, 96)  # a green color for the buttons
RED = (255, 0, 0)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class GameOver:
    def __init__(self, screen, player,size):
        self.screen = screen
        self.font = pygame.font.Font(None, 20)
        self.player = player
        self.size=size

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Draw the background
            self.screen.fill(BLUE)



            # Draw the game over text
            game_over_text = self.font.render("Game Over", True, RED)
            self.screen.blit(game_over_text, ((self.size - game_over_text.get_width()) // 2 + 190, 100))

            score_text = self.font.render(f"Your score: {self.player.score}", True, (0, 0, 0))
            self.screen.blit(score_text, ((self.size  - score_text.get_width()) // 2 + 190, 150))

            instructions_text = self.font.render("Press  Q to quit", True, (0, 0, 0))
            self.screen.blit(instructions_text, ((self.size - instructions_text.get_width()) // 2 + 200, 200))

           



            # Update the display
            pygame.display.update()

            # Handle key presses
            keys = pygame.key.get_pressed()
           
            if keys[pygame.K_q]:
                pygame.quit()
                sys.exit()

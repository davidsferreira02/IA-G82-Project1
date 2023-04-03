import pygame
import sys
from arena import Arena

class GameOptionsMenu:
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
    
    
    def __init__(self, size):
        # Initialize Pygame
        pygame.init()
        self.size = size
        self.font = pygame.font.SysFont(None, 30)
        self.clock = pygame.time.Clock()
        # Create the screen
        self.screen = pygame.display.set_mode(
            (self.ARENA_WIDTH * self.BLOCK_SIZE, self.ARENA_HEIGHT * self.BLOCK_SIZE))



    def run(self):
        human_mode_button = pygame.Rect(self.SCREEN_WIDTH // 2.6 , self.SCREEN_HEIGHT // 2 - 25, 300, 50)
        computer_bfs_button = pygame.Rect(self.SCREEN_WIDTH // 2.6 , self.SCREEN_HEIGHT // 2 + 50 , 300, 50)
        computer_astar_button = pygame.Rect(self.SCREEN_WIDTH // 2.6 , self.SCREEN_HEIGHT // 2 + 120, 300, 50)

         # Define the game loop
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Handle key presses
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if human_mode_button.collidepoint(event.pos):
                        arena=Arena(self.size,0) #modo de jogo normal
                        arena.run()
                    if computer_bfs_button.collidepoint(event.pos): #TODO
                        arena = Arena(self.size,1) #bfs
                    if computer_astar_button.collidepoint(event.pos): 
                        arena = Arena(self.size,2) #astar
                        arena.run()


            # Draw the background
            self.screen.fill(self.WHITE)

            title_text = self.font.render(" Select game mode ", True, self.BLACK)
            self.screen.blit(title_text, (((self.SCREEN_WIDTH // 2 )+80) - title_text.get_width() // 2, 100))

            # Draw the instructions
            human_mode_text = self.font.render("Human mode", True, self.BLACK)
            self.screen.blit(human_mode_text, (human_mode_button.centerx - human_mode_text.get_width() // 2, human_mode_button.centery - human_mode_text.get_height() // 2))

            computer_bfs_text = self.font.render("Computer mode with BFS", True, self.BLACK)
            self.screen.blit(computer_bfs_text, (computer_bfs_button.centerx - computer_bfs_text.get_width() // 2, computer_bfs_button.centery - computer_bfs_text.get_height() // 2))

            computer_astar_text = self.font.render("Computer mode with A*", True, self.BLACK)
            self.screen.blit(computer_astar_text, (computer_astar_button.centerx - computer_astar_text.get_width() // 2, computer_astar_button.centery - computer_astar_text.get_height() // 2))


            # Draw the start button
            pygame.draw.rect(self.screen, self.BLACK, human_mode_button, 2)
            pygame.draw.rect(self.screen, self.BLACK, computer_bfs_button, 2)
            pygame.draw.rect(self.screen, self.BLACK, computer_astar_button, 2)

            # Update the display
            pygame.display.update()

            # Set the frame rate
            self.clock.tick(10)

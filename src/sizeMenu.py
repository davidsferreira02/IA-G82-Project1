
import pygame
import sys
from gameOptionsMenu import GameOptionsMenu 

class SizeMenu:
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

        # Create the screen
        self.screen = pygame.display.set_mode(
            (self.ARENA_WIDTH * self.BLOCK_SIZE, self.ARENA_HEIGHT * self.BLOCK_SIZE))

    def run(self):
        self.font = pygame.font.SysFont(None, 30)
        self.clock = pygame.time.Clock()
        input_box = pygame.Rect(370, 200, 140, 32)
        color_passive = pygame.Color('chartreuse4')
        color_active = pygame.Color('lightskyblue3')
        color = color_passive
        active = False
        text = ''

        # Define the game loop
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_passive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            gameOptionsMenu=GameOptionsMenu(int(text))
                            gameOptionsMenu.run()
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            # Draw the background
            self.screen.fill(self.WHITE)
            if active:
                color = color_active
            else:
                color = color_passive
          
            title_text = self.font.render(" Write arena size (10-20) in rectangle", True, self.BLACK)
            self.screen.blit(title_text, (((self.SCREEN_WIDTH // 2 )+80) - title_text.get_width() // 2, 100))

            pygame.draw.rect(self.screen, color, input_box)
            text_surface = self.font.render(text, True, (255, 255, 255))
            
            width = max(50, text_surface.get_width()+10)
            input_box.w = width
            self.screen.blit(text_surface, (input_box.x+10, input_box.y+5))

            pygame.display.flip()
            self.clock.tick(30)



import random
import pygame
import sys
from player import Player
from astar import Astar

class Arena:
    ARENA_WIDTH_BLOCKS = 10
    ARENA_HEIGHT_BLOCKS = 10
    BLOCK_SIZE = 40
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480

    # Define colors
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GOLD = (255, 215, 0)

    def __init__(self, size):
        # Initialize Pygame
        pygame.init()
        random.seed(1730)
        self.size = size
        self.ARENA_WIDTH_BLOCKS = size
        self.ARENA_HEIGHT_BLOCKS = size

        # Create the screen
        self.screen = pygame.display.set_mode(
            (self.ARENA_WIDTH_BLOCKS * self.BLOCK_SIZE, self.ARENA_HEIGHT_BLOCKS * self.BLOCK_SIZE))

        # Create the player
        self.player = Player("Player", 0, 0, 'UP')

        # Set the clock
        self.clock = pygame.time.Clock()

        # Set the font
        self.font = pygame.font.SysFont(None, 30)

        # Create initial blocks
        self.black_blocks = []
        for i in range(random.randint(1, 30)):
            x = random.randint(0, self.ARENA_WIDTH_BLOCKS-1)
            y = random.randint(0, self.ARENA_HEIGHT_BLOCKS-1)
            while ((x,y) in self.black_blocks or (x,y) == (self.player.x, self.player.y)):
                x = random.randint(0, self.ARENA_WIDTH_BLOCKS-1)
                y = random.randint(0, self.ARENA_HEIGHT_BLOCKS-1)
            self.black_blocks.append((x, y))

        self.golden_block = (random.randint(0, self.ARENA_WIDTH_BLOCKS-1),
                            random.randint(0, self.ARENA_HEIGHT_BLOCKS-1))
        
        while (self.golden_block in self.black_blocks or self.golden_block == (self.player.x, self.player.y)) :
            self.golden_block = (random.randint(0, self.ARENA_WIDTH_BLOCKS-1), random.randint(0, self.ARENA_HEIGHT_BLOCKS-1))

        self.golden_block_X = self.golden_block[0]
        self.golden_block_Y = self.golden_block[1] 

        self.score_level = 0     

        self.astar=Astar() 
              

    def run(self):
        res=[]
        res = res = self.astar.find_path((self.player.x, self.player.y), self.golden_block, self.ARENA_WIDTH_BLOCKS, self.ARENA_HEIGHT_BLOCKS, self.black_blocks)

        res1=len(res)
       
        # Define the game loop
        while True:
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if(self.player.x == self.golden_block_X and self.player.y == self.golden_block_Y and self.player.state == 'UP'): 
                    self.player.update_score()   

                # Handle key presses
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if (self.player.x-1, self.player.y) not in self.black_blocks:
                            if (self.player.state == 'DS'):
                                self.player.move_left()
                            elif ((self.player.state == 'DF') and (self.player.x-1, self.player.y+1) not in self.black_blocks):
                                self.player.move_left() 
                            elif ((self.player.state == 'UP') and (self.player.x-2, self.player.y) not in self.black_blocks):
                                self.player.move_left()            
                    elif event.key == pygame.K_RIGHT:
                        if (self.player.state == 'DS'):
                            if (self.player.x+2, self.player.y) not in self.black_blocks:    
                                self.player.move_right()
                        elif (self.player.x+1, self.player.y) not in self.black_blocks:
                            if ((self.player.state == 'DF') and (self.player.x+1, self.player.y+1) not in self.black_blocks):
                                self.player.move_right()
                            elif ((self.player.state == 'UP') and (self.player.x+2, self.player.y) not in self.black_blocks):
                                self.player.move_right()
                    elif event.key == pygame.K_UP:
                        if (self.player.x, self.player.y-1) not in self.black_blocks:
                            if (self.player.state == 'DF'):
                                self.player.move_up()
                            elif ((self.player.state == 'DS') and (self.player.x+1, self.player.y-1) not in self.black_blocks):
                                self.player.move_up()
                            elif ((self.player.state == 'UP') and (self.player.x, self.player.y-2) not in self.black_blocks):
                                self.player.move_up()
                    elif event.key == pygame.K_DOWN:  
                        if (self.player.state == 'DF'):
                            if (self.player.x, self.player.y + 2) not in self.black_blocks:
                                self.player.move_down()
                        elif (self.player.x, self.player.y + 1) not in self.black_blocks:
                            if ((self.player.state == 'DS') and (self.player.x+1, self.player.y+1) not in self.black_blocks):
                                self.player.move_down()
                            elif ((self.player.state == 'UP') and (self.player.x, self.player.y+2) not in self.black_blocks):
                                self.player.move_down()   

                # Update level and blocks
                if self.player.score > self.player.level:
                    self.player.update_level()
                    
                    self.black_blocks = []
                    for i in range(random.randint(1, 30)):
                        x = random.randint(0, self.ARENA_WIDTH_BLOCKS-1)
                        y = random.randint(0, self.ARENA_HEIGHT_BLOCKS-1)
                        while ((x,y) in self.black_blocks or (x,y) == (self.player.x, self.player.y)):
                            x = random.randint(0, self.ARENA_WIDTH_BLOCKS-1)
                            y = random.randint(0, self.ARENA_HEIGHT_BLOCKS-1)
                        self.black_blocks.append((x, y))
                        self.golden_block = (random.randint(0, self.ARENA_WIDTH_BLOCKS-1),
                                            random.randint(0, self.ARENA_HEIGHT_BLOCKS-1))
                        while (self.golden_block in self.black_blocks or self.golden_block == (self.player.x, self.player.y)) :
                            self.golden_block = (random.randint(0, self.ARENA_WIDTH_BLOCKS-1), random.randint(0, self.ARENA_HEIGHT_BLOCKS-1))
                        self.golden_block_X = self.golden_block[0]
                        self.golden_block_Y = self.golden_block[1]
                        res = res = self.astar.find_path((self.player.x, self.player.y), self.golden_block, self.ARENA_WIDTH_BLOCKS, self.ARENA_HEIGHT_BLOCKS, self.black_blocks)
                        res1=len(res)  

            # Draw the background
            self.screen.fill(self.GRAY)

            for block in self.black_blocks:
               block_rect = pygame.Rect(
                block[0] * self.BLOCK_SIZE, block[1] * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
               pygame.draw.rect(self.screen, self.BLACK, block_rect)
    
            golden_rect = pygame.Rect(
            self.golden_block[0] * self.BLOCK_SIZE, self.golden_block[1] * self.BLOCK_SIZE, self.BLOCK_SIZE,  self.BLOCK_SIZE)
            pygame.draw.rect(self.screen, self.GOLD, golden_rect)

            # Draw the black background
            background_rect = pygame.Rect(self.ARENA_WIDTH_BLOCKS*self.BLOCK_SIZE, 0, self.SCREEN_WIDTH,  self.SCREEN_HEIGHT+500)
            pygame.draw.rect(self.screen, self.BLACK, background_rect)
            background_rect = pygame.Rect(0, self.ARENA_WIDTH_BLOCKS*self.BLOCK_SIZE, self.SCREEN_WIDTH,  self.SCREEN_HEIGHT)
            pygame.draw.rect(self.screen, self.BLACK, background_rect)
            
            # Draw the grid
            for i in range(self.ARENA_WIDTH_BLOCKS):
                for j in range(self.ARENA_HEIGHT_BLOCKS):
                    rect = pygame.Rect(i * self.BLOCK_SIZE, j *
                                    self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
                    pygame.draw.rect(self.screen, self.BLACK, rect, 1)


            # Draw the player
            player_rect = pygame.Rect(self.player.x * self.BLOCK_SIZE,
                              self.player.y * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
            pygame.draw.rect(self.screen, self.RED, player_rect)
            if self.player.state == 'DS':
                player_rect = pygame.Rect((self.player.x+1) * self.BLOCK_SIZE,
                              self.player.y * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
                pygame.draw.rect(self.screen, self.RED, player_rect)
            elif self.player.state == 'DF':
                player_rect = pygame.Rect(self.player.x * self.BLOCK_SIZE,
                              (self.player.y+1) * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
                pygame.draw.rect(self.screen, self.RED, player_rect)

            # Draw the score
            score_text = self.font.render(f"Score: {self.player.score}", True,self.WHITE)
            self.screen.blit(score_text, (10, 10))
            level_text = self.font.render(f"Level: {self.player.level}", True, self.WHITE)
            self.screen.blit(level_text, (10, 30))
            cost_text = self.font.render(f"cost: {self.player.cost}", True, self.WHITE)
            self.screen.blit(cost_text, (10, 50))
            top_text = self.font.render(f"par: {res1}", True, self.WHITE)
            self.screen.blit(top_text, (10, 70))
          

            # Update the display
            pygame.display.update()

            # Set the frame rate
            self.clock.tick(10)


import random
import pygame
import sys
from player import Player
from astar import Astar



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

  



    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Create the screen
        self.screen = pygame.display.set_mode(
            (self.ARENA_WIDTH * self.BLOCK_SIZE, self.ARENA_HEIGHT * self.BLOCK_SIZE))

        # Create the player
        self.player = Player([(0,0),(0,3),(1,0),(1,3)])

        


        # Set the clock
        self.clock = pygame.time.Clock()

        # Set the font
        self.font = pygame.font.SysFont(None, 30)

        # Create initial blocks
        self.black_blocks = []
        for i in range(random.randint(1, 30)):
            j=0
            while j==0:
             x = random.randint(0, self.ARENA_WIDTH-1)
             y = random.randint(0, self.ARENA_HEIGHT-3)
             if(x,y) not in self.player.block:
              self.black_blocks.append((x, y))
              j=1

            j=0
            while j==0:
             self.golden_block = (random.randint(0, self.ARENA_WIDTH-1),
                            random.randint(0, self.ARENA_HEIGHT-3))
             if(self.golden_block[0],self.golden_block[1]) not in self.black_blocks:
                if(self.golden_block[0],self.golden_block[1]) not in self.player.block:  
                    self.golden_block_X = self.golden_block[0]
                    self.golden_block_Y = self.golden_block[1] 
                    j=1
                    


        self.score_level = 0     

        self.astar=Astar() 
        res=[]
        res1=0

              

    def run(self):
     

       

       
       
        # Define the game loop
     while True:
        

    
        
           
            
            # Handle events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                 


                    

                if (player_rect.x==golden_rect.x and player_rect.y==golden_rect.y):
                    self.player.update_score()
                
               
                

                # Handle key presses
                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_LEFT:
                    if all((self.player.get_left()-i, self.player.get_y()-j) not in self.black_blocks
                      for i in range(2) for j in range(-2, 3)):
                        self.player.move_left()
                  elif event.key == pygame.K_RIGHT:
                    if all((self.player.get_right() + i, self.player.get_y()-j) not in self.black_blocks
                      for i in range(1) for j in range(-2, 3)):
                        self.player.move_right()
                  elif event.key == pygame.K_UP:
                    if all((self.player.get_x(), self.player.get_top() - j) not in self.black_blocks
                      for j in range(1,4)):
                        self.player.move_up()
                  elif event.key == pygame.K_DOWN:
                     if all((self.player.get_x(), self.player.get_bottom() + j) not in self.black_blocks
                      for j in range(1)):
                       self.player.move_down()

                    

                  
                    
                            
                    
                    

                # Update level and blocks
                if self.player.score > self.player.level:
                    self.player.update_level()
                    
                    self.black_blocks = []
                    for i in range(random.randint(1, 30)):
                         j=0  
                         while j==0:
                             
                          x = random.randint(0, self.ARENA_WIDTH)
                          y = random.randint(0, self.ARENA_HEIGHT-3)
                          if(x,y) not in self.black_blocks:
                            if(x,y) not in self.player.block:
                             self.black_blocks.append((x, y))
                             self.golden_block = (random.randint(0, self.ARENA_WIDTH),
                                            random.randint(0, self.ARENA_HEIGHT-3))
                             self.golden_block_X = self.golden_block[0]
                             self.golden_block_Y = self.golden_block[1]
                             j=1

                            
                            
                        



        
                        

            # Draw the background
        self.screen.fill(self.GRAY)

        for block in self.black_blocks:
               block_rect = pygame.Rect(
             block[0] * self.BLOCK_SIZE, block[1] * self.BLOCK_SIZE,self.BLOCK_SIZE, 3*self.BLOCK_SIZE)
               pygame.draw.rect(self.screen, self.BLACK, block_rect)

    #draw the gold
        golden_rect = pygame.Rect(
            self.golden_block[0] * self.BLOCK_SIZE, self.golden_block[1] * self.BLOCK_SIZE, self.BLOCK_SIZE,3*self.BLOCK_SIZE )
        pygame.draw.rect(self.screen, self.GOLD, golden_rect)
            

       




     # Draw the grid
        for i in range(self.ARENA_WIDTH):
              for j in range(self.ARENA_HEIGHT):
                rect = pygame.Rect(i * self.BLOCK_SIZE, j *
                                self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)


   # Draw the player
        player_rect = pygame.Rect(min(self.player.block, key=lambda v: v[0])[0] * self.BLOCK_SIZE,
                          min(self.player.block, key=lambda v: v[1])[1] * self.BLOCK_SIZE,
                          self.BLOCK_SIZE,  3*self.BLOCK_SIZE)
        pygame.draw.rect(self.screen, self.RED, player_rect)

            


            
                 

    # Draw the score
        score_text = self.font.render(f"Score: {self.player.score}", True,self.WHITE)
        self.screen.blit(score_text, (10, 10))
        level_text = self.font.render(f"Level: {self.player.level}", True, self.WHITE)
        self.screen.blit(level_text, (10, 30))
        cost_text = self.font.render(f"cost: {self.player.cost}", True, self.WHITE)
        self.screen.blit(cost_text, (10, 50))
        top_text = self.font.render(f"par: { len(self.astar.find_path((player_rect.x,player_rect.y), self.golden_block, self.ARENA_WIDTH, self.ARENA_HEIGHT, self.black_blocks))}", True, self.WHITE)
        self.screen.blit(top_text, (10, 70))
            
           

    # Update the display
        pygame.display.update()

    # Set the frame rate
        self.clock.tick(10)

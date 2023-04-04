import random
import pygame
import sys
from player import Player
from astar import get_path

def next_level(player_x,player_y,player_state, golden_block_X, golden_block_Y):
    print("player_x",player_x)
    print("y",player_y)
    print("state",player_state)
    print("goldenb_x",golden_block_X)
    print("goldenb_y",golden_block_Y)
    if(player_x == golden_block_X and player_y == golden_block_Y and player_state == 'UP'): 
        return True
    else:
        return False  
def update_level_and_blocks(player_x,player_y,arena_width, arena_height):
# Update level and blocks
    black_blocks = []
    for i in range(random.randint(1, 30)):
        x = random.randint(0, arena_width-1)
        y = random.randint(0, arena_height-1)
        while ((x,y) in black_blocks or (x,y) == (player_x, player_y)):
            x = random.randint(0, arena_width-1)
            y = random.randint(0, arena_height-1)

        black_blocks.append((x, y))
        
    golden_block = (random.randint(0, arena_width-1),
                        random.randint(0, arena_height-1))
    
    while (golden_block in black_blocks or golden_block == (player_x,player_y)) :
        golden_block = (random.randint(0, arena_width-1), random.randint(0, arena_height-1))

    return (golden_block,black_blocks)

        
def draw_background(screen,black_blocks,golden_block,block_size,screen_width,screen_height,arena_width,arena_height,black,gray,gold):
    # Draw the background
    screen.fill(gray)

    for block in black_blocks:
        block_rect = pygame.Rect(
        block[0] * block_size, block[1] * block_size, block_size,block_size)
        pygame.draw.rect(screen, black, block_rect)

    golden_rect = pygame.Rect(
    golden_block[0] * block_size, golden_block[1] * block_size, block_size, block_size)
    pygame.draw.rect(screen, gold, golden_rect)

    # Draw the black background
    background_rect = pygame.Rect(arena_width*block_size, 0, screen_width,  screen_height+500)
    pygame.draw.rect(screen, black, background_rect)
    background_rect = pygame.Rect(0, arena_width*block_size, screen_width,  screen_height)
    pygame.draw.rect(screen, black, background_rect)

    # Draw the grid
    for i in range(arena_width):
        for j in range(arena_height):
            rect = pygame.Rect(i * block_size, j *
                            block_size, block_size, block_size)
            pygame.draw.rect(screen, black, rect, 1)

def draw_player(player_x,player_state,player_y,block_size,red,screen):
# Draw the player
    player_rect = pygame.Rect(player_x * block_size,
                        player_y * block_size, block_size, block_size)
    pygame.draw.rect(screen, red, player_rect)
    if player_state == 'DS':
        player_rect = pygame.Rect((player_x+1) * block_size,
                        player_y * block_size, block_size, block_size)
        pygame.draw.rect(screen, red, player_rect)
    elif player_state == 'DF':
        player_rect = pygame.Rect(player_x * block_size,
                        (player_y+1) * block_size, block_size, block_size)
        pygame.draw.rect(screen, red, player_rect)

def draw_score(player_score,white,screen,player_cost,player_level,font,clock):
    # Draw the score
    score_text = font.render(f"Score: {player_score}", True, white)
    screen.blit(score_text, (10, 10))
    level_text = font.render(f"Level: {player_level}", True, white)
    screen.blit(level_text, (10, 30))
    cost_text = font.render(f"cost: {player_cost}", True, white)
    screen.blit(cost_text, (10, 50))
    #top_text = self.font.render(f"par: {res1}", True, self.WHITE)
    #self.screen.blit(top_text, (10, 70))


# Update the display
    pygame.display.update()
    pygame.time.delay(520)
    # Set the frame rate
    #clock.tick(10)

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

    def __init__(self, size, game_mode,seed):
        # Initialize Pygame
        pygame.init()
        random.seed(seed)
        self.size = size
        self.ARENA_WIDTH_BLOCKS = size
        self.ARENA_HEIGHT_BLOCKS = size
        self.game_mode = game_mode

        # Create the screen
        self.screen = pygame.display.set_mode(
            (self.ARENA_WIDTH_BLOCKS * self.BLOCK_SIZE, self.ARENA_HEIGHT_BLOCKS * self.BLOCK_SIZE))

        # Create the player
        self.player = Player("Player", 0, 0, 'UP', size)

        # Set the clock
        self.clock = pygame.time.Clock()

        # Set the font
        self.font = pygame.font.SysFont(None, 30)

        # Create initial blocks
        self.golden_block,self.black_blocks = update_level_and_blocks(self.player.x, self.player.y, self.ARENA_WIDTH_BLOCKS,self.ARENA_HEIGHT_BLOCKS)
        self.golden_block_X = self.golden_block[0]
        self.golden_block_Y = self.golden_block[1]


        self.score_level = 0   

  
    def run(self):
        # Define the game loop
        while True:
            if(self.game_mode == 0):
            # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    passed_level = next_level(self.player.x,self.player.y,self.player.state, self.golden_block_X, self.golden_block_Y)
                    if passed_level :
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
                            if (self.player.x+1, self.player.y) not in self.black_blocks:
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

                    if self.player.score > self.player.level:
                        self.player.update_level()

                        self.golden_block,self.black_blocks = update_level_and_blocks(self.player.x, self.player.y, self.ARENA_WIDTH_BLOCKS,self.ARENA_HEIGHT_BLOCKS)
                        #print(golden_block)
                        self.golden_block_X = self.golden_block[0]
                        self.golden_block_Y = self.golden_block[1]
                        
                        
                draw_background(self.screen,self.black_blocks,self.golden_block,self.BLOCK_SIZE,self.SCREEN_WIDTH,self.SCREEN_HEIGHT,self.ARENA_WIDTH_BLOCKS,self.ARENA_HEIGHT_BLOCKS,self.BLACK,self.GRAY,self.GOLD)
                draw_player(self.player.x,self.player.state,self.player.y,self.BLOCK_SIZE,self.RED,self.screen)
                draw_score(self.player.score,self.WHITE,self.screen,self.player.cost,self.player.level,self.font,self.clock)

            elif (self.game_mode == 1): #bfs
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    #print(self.player.x)
                    passed_level = next_level(self.player.x,self.player.y,self.player.state, self.golden_block_X, self.golden_block_Y)

                    if passed_level:
                        self.player.update_level()
                        #print(self.player.score)
                    else:
                        #path = get_path((self.player.x, self.player.y), self.golden_block, self.black_blocks, self.ARENA_WIDTH_BLOCKS, self.ARENA_HEIGHT_BLOCKS)
                        for new_coordinates in path:
                            self.player.x = new_coordinates[0]
                            self.player.y = new_coordinates[1]
                            draw_background(self.screen,self.black_blocks,self.golden_block,self.BLOCK_SIZE,self.SCREEN_WIDTH,self.SCREEN_HEIGHT,self.ARENA_WIDTH_BLOCKS,self.ARENA_HEIGHT_BLOCKS,self.BLACK,self.GRAY,self.GOLD)
                            draw_player(self.player.x,self.player.state,self.player.y,self.BLOCK_SIZE,self.RED,self.screen)
                            draw_score(self.player.score,self.WHITE,self.screen,self.player.cost,self.player.level,self.font,self.clock)


                    self.golden_block,self.black_blocks = update_level_and_blocks(self.player.x, self.player.y, self.ARENA_WIDTH_BLOCKS,self.ARENA_HEIGHT_BLOCKS)
                    self.golden_block_X = self.golden_block[0]
                    self.golden_block_Y = self.golden_block[1]

            elif (self.game_mode == 2):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    print(self.player.x)
                    passed_level = next_level(self.player.x,self.player.y,self.player.state, self.golden_block_X, self.golden_block_Y)

                    if passed_level:
                        self.player.update_level()
                        #print(self.player.score)
                    else:
                        path = get_path((self.player.x, self.player.y), self.golden_block, self.black_blocks, self.ARENA_WIDTH_BLOCKS, self.ARENA_HEIGHT_BLOCKS)
                        for new_coordinates in path:
                            self.player.x = new_coordinates[0]
                            self.player.y = new_coordinates[1]
                            draw_background(self.screen,self.black_blocks,self.golden_block,self.BLOCK_SIZE,self.SCREEN_WIDTH,self.SCREEN_HEIGHT,self.ARENA_WIDTH_BLOCKS,self.ARENA_HEIGHT_BLOCKS,self.BLACK,self.GRAY,self.GOLD)
                            draw_player(self.player.x,self.player.state,self.player.y,self.BLOCK_SIZE,self.RED,self.screen)
                            draw_score(self.player.score,self.WHITE,self.screen,self.player.cost,self.player.level,self.font,self.clock)


                    self.golden_block,self.black_blocks = update_level_and_blocks(self.player.x, self.player.y, self.ARENA_WIDTH_BLOCKS,self.ARENA_HEIGHT_BLOCKS)
                    self.golden_block_X = self.golden_block[0]
                    self.golden_block_Y = self.golden_block[1]

                            

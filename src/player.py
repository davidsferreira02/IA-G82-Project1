import pygame

ARENA_WIDTH = 20
ARENA_HEIGHT = 15
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 70
BLOCK_SIZE = 40


class Player:

    
    
    

    def __init__(self,name,x,y):
        self.score=0
        self.x=0
        self.y=0
        self.level=1    
 

    def update_score(self):
        self.score+=1 

    def move_up(self):
        if(self.y>0):
            self.y -=1   
    def move_left(self):
        if(self.x>0):
           self.x -= 1  
    def move_right(self):
        if(self.x <ARENA_WIDTH -1):
            self.x +=1   

    def move_down(self):
        if (self.y <ARENA_HEIGHT -1):
            self.y += 1

    def update_level(self):
        self.level+=1
     
    def _str(self):
        return f"{self.name}:{self.score}"           



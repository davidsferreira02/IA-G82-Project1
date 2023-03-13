import pygame

class Player:

    def __init__(self,name,x,y):
        self.score=0
        self.x=0
        self.y=0
        self.level=1
    
 

    def update_score(self):
        self.score+=1 

    def move_up(self):
        self.y -=1   
    def move_left(self):
        self.x -= 1  
    def move_right(self):
        self.x +=1   

    def move_down(self):
        self.y += 1

    def update_level(self):
        self.level+=1
     
    def _str(self):
        return f"{self.name}:{self.score}"           



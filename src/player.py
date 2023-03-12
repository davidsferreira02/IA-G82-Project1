import pygame

class Player:

    def __init__(self,name,x,y):
        self.name=name
        self.score=0
        self.x=0
        self.y=0
        self.level=1


    def get_name(self):
        return self.name  

    def get_score(self): 
        return self.score

    def get_level(self):
        return self.level    

    def update_score(self,points):
        self.score+=points 

    def move_up(self):
        self.y -=1   
    def move_left(self):
        self.x -= 1  
    def move_right(self):
        self.x +=1   

    def move_down(self):
        self.y += 1   


    def _str(self):
        return f"{self.name}:{self.score}"           



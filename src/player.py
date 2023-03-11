import pygame

class Player:

    def player(self,name):
        self.name=name
        self.score=0


    def get_name(self):
        return self.name  

    def get_score(self): 
        return self.score

    def update_score(self,points):
        self.score+=points 


    def _str(self):
        return f"{self.name}:{self.score}"           



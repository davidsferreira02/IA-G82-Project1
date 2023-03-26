ARENA_WIDTH = 10
ARENA_HEIGHT = 10
BLOCK_SIZE = 40

class Player:

    def __init__(self, name, x, y, state):
        self.score=0
        self.x=0
        self.y=0
        self.level=1 
        self.cost=0
        self.state='UP'

    def update_score(self):
        self.score+=1 

    def update_cost(self):
        self.cost+=1

    def reset_cost(self):
        self.cost=0       

    def move_up(self):
        self.update_cost()
        if(self.y>0):
            self.y -=1

    def move_left(self):
        self.update_cost()
        if(self.x>0):
           self.x -= 1  


    def move_right(self):
        self.update_cost()
        if((self.x + 1) < ARENA_WIDTH):
            self.x +=1   

    def move_down(self):
        self.update_cost()
        if ((self.y+1) < ARENA_HEIGHT):
            self.y += 1

    def update_level(self):
        self.level+=1
        self.reset_cost()

    


          
            


     

 
    
    
       




    def _str(self):
        return f"{self.name}:{self.score}"           



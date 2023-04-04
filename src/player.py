BLOCK_SIZE = 40

class Player:

    def __init__(self, x, y, state, size):
        self.score=0
        self.x=x
        self.y=y
        self.level=0
        self.cost=0
        self.state=state
        self.size = size

    def update_score(self):
        self.score+=1 

    def update_cost(self):
        self.cost+=1

    def reset_cost(self):
        self.cost=0

    def reset_level(self):
        self.level=0

    def reset_score(self):
        self.score=0

    def reset_position(self):
        self.x=0
        self.y=0  
    def reset_state(self):
        self.state="UP"                     


            
                
               
            
    def move_up(self):
        self.update_cost()
        if (self.state == 'UP' and self.y-1>0):
            self.state = 'DF'
            self.y -= 2
        elif (self.state == 'DF' and self.y>0):
            self.state = 'UP'
            self.y -=1
        elif (self.state == 'DS' and self.y>0):
            self.y -=1

    def move_left(self):
        self.update_cost()
        if (self.state == 'UP' and self.x-1>0):
            self.state = 'DS'
            self.x -= 2
        elif (self.state == 'DF' and self.x>0):
            self.x -=1
        elif (self.state == 'DS' and self.x>0):
            self.state = 'UP'
            self.x -=1

    def move_right(self):
        self.update_cost()
        if (self.state == 'UP' and (self.x + 2) < self.size):
            self.state = 'DS'
            self.x += 1
        elif (self.state == 'DF' and (self.x + 1) < self.size):
            self.x +=1
        elif (self.state == 'DS' and (self.x + 2) < self.size):
            self.state = 'UP'
            self.x +=2

    def move_down(self):
        self.update_cost()
        if (self.state == 'UP' and self.y+2 < self.size):
            self.state = 'DF'
            self.y += 1
        elif (self.state == 'DF' and (self.y+1) < self.size-1):
            self.state = 'UP'
            self.y +=2
        elif (self.state == 'DS' and (self.y+1) < self.size):
            self.y +=1

    def update_level(self):
        self.level+=1
        self.reset_cost()

    


          
            


     

 
    
    
       


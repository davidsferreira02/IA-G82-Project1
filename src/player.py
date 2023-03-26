import pygame

ARENA_WIDTH = 20
ARENA_HEIGHT = 15
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 70
BLOCK_SIZE = 40



class Player:
    def __init__(self, block):
        self.score = 0
        self.block = block
        self.level = 1
        self.cost = 0
        
        
    def update_score(self):
        self.score += 1

    def update_cost(self):
        self.cost += 1

    def reset_cost(self):
        self.cost = 0


    def move_up(self):
        self.update_cost()
        if self.get_top() > 0:
            self.set_y(self.get_y() - 1)

    def move_left(self):
        self.update_cost()
        if self.get_left() > 0 :
            self.set_x(self.get_x() - 1)

    def move_right(self):
        self.update_cost()
        if self.get_right() < ARENA_WIDTH-1 :
            self.set_x(self.get_x() + 1)

    def move_down(self):
        self.update_cost()
        if self.get_bottom() < ARENA_HEIGHT  :
            self.set_y(self.get_y() + 1)

    def update_level(self):
        self.level += 1
        self.reset_cost()

    def get_x(self):
        return self.block[0][0]

    def get_y(self):
        return self.block[0][1]

    def set_x(self, x):
        dx = x - self.get_x()
        dy = 0
        self.block = [(x, y) for (x, y) in self.block]
        self.update_block(dx, dy)

    def set_y(self, y):
        dx = 0
        dy = y - self.get_y()
        self.block = [(x, y) for (x, y) in self.block]
        self.update_block(dx, dy)

    def update_block(self, dx, dy):
        self.block = [(x + dx, y + dy) for (x, y) in self.block]

    def get_left(self):
        return min([x for (x, y) in self.block])

    def get_right(self):
        return max([x for (x, y) in self.block])

    def get_top(self):
        return min([y for (x, y) in self.block])

    def get_bottom(self):
        return max([y for (x, y) in self.block])

             



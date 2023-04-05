

class BfsNode:
    def __init__(self, pos: tuple, direction: int, parent = None):
        
        """
        0 -> up (deitado)
        1 -> right
        2 -> down
        3 -> left 
        4 -> standing
        """
        self.pos = pos
        self.direction = direction
        self.parent = parent
        self.children = []


    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self
    """
    def create_children(self):
        up = self.rotate_up()
        down = self.rotate_down()
        left = self.rotate_left()
        right = self.rotate_right()
        if up != None:
            self.add_child(BfsNode(up, 0,self))
        if down != None:
            self.add_child(BfsNode(down,2,self))
        if left != None:
            self.add_child(BfsNode(left,3,self))
        if right != None:
            self.add_child(BfsNode(right,1,self))

"""
    def rotate_up(self): 
        if self.direction == 0:
            return BfsNode((self.pos[0], self.pos[1]-2), 4, self)
        elif self.direction == 1:
            return BfsNode((self.pos[0], self.pos[1]-1), 1, parent=self)
        elif self.direction == 2:
            return BfsNode((self.pos[0], self.pos[1]-1), 4, parent=self)
        elif self.direction == 3:
            return BfsNode((self.pos[0], self.pos[1]-1), 3, parent=self)
        else:
            return BfsNode((self.pos[0], self.pos[1]-1), 0, parent=self)

    def rotate_right(self):
        if self.direction == 0:
            return BfsNode((self.pos[0]+1, self.pos[1]), 0, parent=self)
        elif self.direction == 1:
            return BfsNode((self.pos[0]+2, self.pos[1]), 4, parent=self)
        elif self.direction == 2:
            return BfsNode((self.pos[0]+1, self.pos[1]), 2, parent=self)
        elif self.direction == 3:
            return BfsNode((self.pos[0]+1, self.pos[1]), 4, parent=self)
        else:
            return BfsNode((self.pos[0]+1, self.pos[1]), 1, parent=self)

    def rotate_down(self):
        if self.direction == 0:
            return BfsNode((self.pos[0], self.pos[1]+1), 4, parent=self)
        elif self.direction == 1:
            return BfsNode((self.pos[0], self.pos[1]+1), 1, parent=self)
        elif self.direction == 2:
            return BfsNode((self.pos[0], self.pos[1]+2), 4, parent=self)
        elif self.direction == 3:
            return BfsNode((self.pos[0], self.pos[1]+1), 3, parent=self)
        else:
            return BfsNode((self.pos[0], self.pos[1]+2), 2, parent=self)

    def rotate_left(self): 
        if self.direction == 0:
            return BfsNode((self.pos[0]-1, self.pos[1]), 0, parent=self)
        elif self.direction == 1:
            return BfsNode((self.pos[0]-1, self.pos[1]), 4, parent=self)
        elif self.direction == 2:
            return BfsNode((self.pos[0]-1, self.pos[1]), 2, parent=self)
        elif self.direction == 3:
            return BfsNode((self.pos[0]-2, self.pos[1]), 4, parent=self)
        else:
            return BfsNode((self.pos[0]-1, self.pos[1]), 3, parent=self)
    
    def get_occupation(self):
        res = [self.pos]
        if self.direction == 0:
            res.append((self.pos[0], self.pos[1]-1))
        elif self.direction == 1:
            res.append((self.pos[0]+1, self.pos[1]))
        elif self.direction == 2:
            res.append((self.pos[0], self.pos[1]+1))
        elif self.direction == 3:
            res.append((self.pos[0]-1, self.pos[1]))

        return res
    
    def set_parent(self, parent):
        self.parent = parent
  

def bfs(player_node: tuple, goal_node: tuple, obstacles: list, width: int, height: int) :
    # Create a queue and add the starting node to it
    queue = []
    start_node = BfsNode(player_node, 4)
    queue.append(start_node)
    # store the visited nodes
    visited = [start_node]

    # Loop until the queue is empty
    while queue:
        # Get the next node from the queue
        current_node = queue.pop(0)

        # Check if we have reached the goal node
        if current_node.pos == goal_node:
            # We have found the shortest path, so return the distance
            return current_node

        # Generate the children nodes and add them to the queue if they haven't been visited
        children = []

        children.append(BfsNode(current_node,0))
        children.append(BfsNode(current_node,1))
        children.append(BfsNode(current_node,2))
        children.append(BfsNode(current_node,3))

        for child in children:
            print(child.pos)
            if child not in visited and child not in obstacles:
                visited.append(child)
                queue.append(child)

    # If we reach this point, there is no path from the starting node to the goal node
    return -1


        





def get_path_bfs(start, goal, obstacles, width, height):
    BfsNode = bfs(start, goal, obstacles, width, height)  
    succ = BfsNode
    path = []

    while succ != None:
        path.append(succ.pos)
        succ = succ.parent

    path.reverse()

    return path
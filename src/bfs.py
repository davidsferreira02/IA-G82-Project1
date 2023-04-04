import heapq
from queue import Queue

"""
1.  Initialize the open list
2.  Initialize the closed list
    put the starting node on the open 
    list (you can leave its f at zero)
3.  while the open list is not empty
    a) find the node with the least f on 
       the open list, call it "q"
    b) pop q off the open list
  
    c) generate q's 8 successors and set their 
       parents to q
   
    d) for each successor
        i) if successor is the goal, stop search
        
        ii) else, compute both g and h for successor
          successor.g = q.g + distance between 
                              successor and q
          successor.h = distance from goal to 
          successor (This can be done using many 
          ways, we will discuss three heuristics- 
          Manhattan, Diagonal and Euclidean 
          Heuristics)
          
          successor.f = successor.g + successor.h
        iii) if a node with the same position as 
            successor is in the OPEN list which has a 
           lower f than successor, skip this successor
        iV) if a node with the same position as 
            successor  is in the CLOSED list which has
            a lower f than successor, skip this successor
            otherwise, add  the node to the open list
     end (for loop)
  
    e) push q on the closed list
    end (while loop)
"""  
class BfsNode:
    def __init__(self, pos: tuple, direction: int, f: int = 0, parent = None):
        
        """
        0 -> up (deitado)
        1 -> right
        2 -> down
        3 -> left 
        4 -> standing
        """
        self.pos = pos
        self.direction = direction
        self.h = 0
        self.g = 0
        self.f = f
        self.parent = parent
    
    def __lt__(self, other):
        return self.f < other.f

    def rotate_up(self): 
        if self.direction == 0:
            return BfsNode((self.pos[0], self.pos[1]-2), 4, parent=self)
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
    
    def set_g(self, g: int):
        self.g = g
        self.f = self.g + self.h
    
    def set_h(self, h):
        self.h = h
        self.f = self.g + self.h #f depende do h

    
      




def bfs(player_node: tuple[int, int], goal_node: tuple[int, int], obstacles: list[tuple[int, int]], width: int, height: int) -> int:
    # Create a queue and add the starting node to it
    queue = Queue()
    start_node = BfsNode(player_node, 4)
    queue.put(start_node)

    # Create a set to store the visited nodes
    visited = set()
    visited.add(player_node)

    # Loop until the queue is empty
    while not queue.empty():
        # Get the next node from the queue
        current_node = queue.get()

        # Check if we have reached the goal node
        if current_node.pos == goal_node:
            # We have found the shortest path, so return the distance
            return current_node.g

        # Generate the children nodes and add them to the queue if they haven't been visited
        children = [current_node.rotate_up(), current_node.rotate_right(), current_node.rotate_down(), current_node.rotate_left()]
        for child in children:
            if child.pos not in visited and child.pos not in obstacles:
                visited.add(child.pos)
                child.set_g(current_node.g + 1)
                child.set_h(abs(child.pos[0] - goal_node[0]) + abs(child.pos[1] - goal_node[1]))
                queue.put(child)

    # If we reach this point, there is no path from the starting node to the goal node
    return -1


def get_path(start, goal, obstacles, width, height):
    BfsNode = bfs(start, goal, obstacles, width, height)  
    succ = BfsNode
    path = []

    while succ != None:
        path.append(succ.pos)
        succ = succ.parent

    path.reverse()

    return path


import heapq

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
class AstarNode:
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
            return AstarNode((self.pos[0], self.pos[1]-2), 4, parent=self)
        elif self.direction == 1:
            return AstarNode((self.pos[0], self.pos[1]-1), 1, parent=self)
        elif self.direction == 2:
            return AstarNode((self.pos[0], self.pos[1]-1), 4, parent=self)
        elif self.direction == 3:
            return AstarNode((self.pos[0], self.pos[1]-1), 3, parent=self)
        else:
            return AstarNode((self.pos[0], self.pos[1]-1), 0, parent=self)

    def rotate_right(self):
        if self.direction == 0:
            return AstarNode((self.pos[0]+1, self.pos[1]), 0, parent=self)
        elif self.direction == 1:
            return AstarNode((self.pos[0]+2, self.pos[1]), 4, parent=self)
        elif self.direction == 2:
            return AstarNode((self.pos[0]+1, self.pos[1]), 2, parent=self)
        elif self.direction == 3:
            return AstarNode((self.pos[0]+1, self.pos[1]), 4, parent=self)
        else:
            return AstarNode((self.pos[0]+1, self.pos[1]), 1, parent=self)

    def rotate_down(self):
        if self.direction == 0:
            return AstarNode((self.pos[0], self.pos[1]+1), 4, parent=self)
        elif self.direction == 1:
            return AstarNode((self.pos[0], self.pos[1]+1), 1, parent=self)
        elif self.direction == 2:
            return AstarNode((self.pos[0], self.pos[1]+2), 4, parent=self)
        elif self.direction == 3:
            return AstarNode((self.pos[0], self.pos[1]+1), 3, parent=self)
        else:
            return AstarNode((self.pos[0], self.pos[1]+2), 2, parent=self)

    def rotate_left(self): 
        if self.direction == 0:
            return AstarNode((self.pos[0]-1, self.pos[1]), 0, parent=self)
        elif self.direction == 1:
            return AstarNode((self.pos[0]-1, self.pos[1]), 4, parent=self)
        elif self.direction == 2:
            return AstarNode((self.pos[0]-1, self.pos[1]), 2, parent=self)
        elif self.direction == 3:
            return AstarNode((self.pos[0]-2, self.pos[1]), 4, parent=self)
        else:
            return AstarNode((self.pos[0]-1, self.pos[1]), 3, parent=self)
    
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



def manhattan_distance(node1: AstarNode, goal_node: tuple):
        return abs(node1.pos[0] - goal_node[0]) + abs(node1.pos[1] - goal_node[1]) 

def astar(player_node: tuple, goal_node: tuple, obstacles: list, width: int, height: int, heuristic = manhattan_distance):
    open_list = []
    closed_list = []

    heapq.heappush(open_list, AstarNode(player_node, 4)) 

    while len(open_list):
        minor_f = heapq.heappop(open_list)

        #gerar para os 4 lados
        dirs = []

        dirs.append(minor_f.rotate_up())
        dirs.append(minor_f.rotate_right())
        dirs.append(minor_f.rotate_down())
        dirs.append(minor_f.rotate_left())

        f_dirs = []
        for dir_ in dirs:
            skipped = False
            for obstacle in obstacles:
                if dir_.pos[0] < 0 or dir_.pos[0] >= width:
                    skipped = True
                    break
                if dir_.pos[1] < 0 or dir_.pos[1] >= height:
                    skipped = True
                    break

                for occupt in dir_.get_occupation():
                    if obstacle[0] == occupt[0] and obstacle[1] == occupt[1]:
                        skipped = True
                        break
            if not skipped:
                f_dirs.append(dir_)


        for sucessor in f_dirs:
            if sucessor.pos[0] == goal_node[0] and sucessor.pos[1] == goal_node[1] and sucessor.direction == 4: # se sucessor e goal com as msmas coordenadas e ta em pe
                return sucessor
            else:
                sucessor.g = minor_f.g + abs(sucessor.pos[0]-minor_f.pos[0]) + abs(sucessor.pos[1]-minor_f.pos[1])
                sucessor.set_h(heuristic(sucessor, goal_node))
                sucessor.f = sucessor.g + sucessor.h
            skipped = False
            for node in open_list:
                if sucessor.pos[0] == node.pos[0] and sucessor.pos[1] == node.pos[1]:
                    if node.f < sucessor.f: 
                        skipped = True
                        break
            
            if skipped: continue
            for node in closed_list:
                if sucessor.pos[0] == node.pos[0] and sucessor.pos[1] == node.pos[1]:
                    if node.f < sucessor.f: 
                        skipped = True
                        break
            
            if skipped: continue
            else:
                heapq.heappush(open_list, sucessor)
        
        closed_list.append(minor_f)

"""
if __name__ == "__main__":
    AstarNode = astar((0, 0), (5, 5), [(1, 1), (2, 3), (2, 4)], 6, 6)"""
def get_path(start, goal, obstacles, width, height):
    AstarNode = astar(start, goal, obstacles, width, height)  
    succ = AstarNode
    path = []

    while succ != None:
        path.append(succ.pos)
        succ = succ.parent

    path.reverse()

    return path


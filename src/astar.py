import heapq

class Astar:
     def __init__(self):
         self.nodes = []
         self.start = None
         self.goal = None
         self.grid_width =None
         self.grid_height = None
         self.obstacles = []
         self.path = []

     def find_path(self, start, goal, grid_width, grid_height, obstacles):
         self.start = start
         self.goal = goal
         self.grid_width = grid_width
         self.grid_height = grid_height
         self.obstacles = obstacles

         self.nodes = []
         for y in range(0,self.grid_height):
             for x in range(0,self.grid_width):
                 self.nodes.append(Node(x, y, self))

         self.start_node = self.get_node(self.start[0], self.start[1])
         self.goal_node = self.get_node(self.goal[0], self.goal[1])

         open_list = []
         closed_list = set()

         heapq.heappush(open_list, (0, self.start_node))
         self.start_node.g = 0

         while open_list:
             current_node = heapq.heappop(open_list)[1]
             closed_list.add(current_node)

             if current_node == self.goal_node:
                 self.path = []
                 while current_node.parent:
                     self.path.append((current_node.x, current_node.y))
                     current_node = current_node.parent
                 self.path.reverse()
                 return self.path

             for neighbor in self.get_neighbors(current_node):
                 if neighbor in closed_list:
                     continue
                 tentative_g_score = current_node.g + 1
                 if neighbor not in open_list:
                     heapq.heappush(open_list, (tentative_g_score + neighbor.distance_to(self.goal_node), neighbor))
                 elif tentative_g_score >= neighbor.g:
                     continue

                 neighbor.parent = current_node
                 neighbor.g = tentative_g_score

         return None

     def get_node(self, x, y):
        
         return self.nodes[y * self.grid_width + x]

     def get_neighbors(self, node):
         neighbors = []
         for x_offset, y_offset in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
             x = node.x + x_offset
             y = node.y + y_offset
             if x < 0 or y < 0 or x >= self.grid_width or y >= self.grid_height:
                 continue
             neighbor = self.get_node(x, y)
             if neighbor in self.obstacles:
                 continue
             neighbors.append(neighbor)
         return neighbors

class Node:
     def __init__(self, x, y, graph):
         self.x = x
         self.y = y
         self.graph = graph
         self.parent = None
         self.g = float('inf')

     def distance_to(self, other):
         return abs(self.x - other.x) + abs(self.y - other.y)

     def __lt__(self, other):
         return False
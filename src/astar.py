from typing import List, Tuple
import heapq

class Node:
    def __init__(self, position: Tuple[int, int], g: int, h: int, parent: 'Node' = None):
        self.position = position
        self.g = g
        self.h = h
        self.parent = parent

    @property
    def f(self) -> int:
        return self.g + self.h

class Arena:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)
    
    def is_valid(self, position: Tuple[int, int]) -> bool:
        x, y = position
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        if self.grid[y][x] == 1:
            return False
        return True

    def get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        x, y = position
        neighbors = []
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if self.is_valid((nx, ny)):
                neighbors.append((nx, ny))
        return neighbors

def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(arena: Arena, start: Tuple[int, int], goal: Tuple[int, int]) -> int:
    start_node = Node(start, 0, heuristic(start, goal))
    open_list = [start_node]
    closed_list = set()

    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return len(path) - 1  # Subtract 1 to remove the start node from the path
        closed_list.add(current_node.position)
        for neighbor_position in arena.get_neighbors(current_node.position):
            if neighbor_position in closed_list:
                continue
            g = current_node.g + 1
            h = heuristic(neighbor_position, goal)
            neighbor_node = Node(neighbor_position, g, h, current_node)
            if neighbor_node.f > g + h:  # This is a faster path to the neighbor
                neighbor_node.g = g
                neighbor_node.parent = current_node
            if neighbor_node not in open_list:
                heapq.heappush(open_list, neighbor_node)

    return 0  # No path found
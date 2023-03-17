from queue import Queue

def bfs(self, start, end):

    visited = set()
    queue = Queue()
    path = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  
    queue.put((start, path))

  
    while not queue.empty():
        
        current, path = queue.get()

        
        if current == end:
            return path

       
        visited.add(current)


        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if neighbor not in visited and \
                    neighbor[0] >= 0 and neighbor[0] < self.ARENA_WIDTH and \
                    neighbor[1] >= 0 and neighbor[1] < self.ARENA_HEIGHT and \
                    neighbor not in self.black_blocks:
                queue.put((neighbor, path + [current]))

    return []

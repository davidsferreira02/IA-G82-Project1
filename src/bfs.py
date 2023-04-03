from collections import deque

class BFS:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, start, goal):
        visited = set()
        queue = deque([(start, [])])

        while queue:
            vertex, path = queue.popleft()
            if vertex == goal:
                return path + [vertex]
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    queue.append((neighbor, path + [vertex]))

        return None

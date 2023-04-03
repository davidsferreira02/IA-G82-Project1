from collections import deque

class Vertex:
    def __init__(self, id):
        self.id = id
        self.adj = []
        self.visited = False

class IntroGraph:
    def __init__(self):
        self.vertexSet = []

    def findVertex(self, id):
        for v in self.vertexSet:
            if v.id == id:
                return v
        return None

    def bfs(self, source):
        res = []
        s = self.findVertex(source)
        if not s:
            return res

        for v in self.vertexSet:
            v.visited = False

        q = deque()
        q.append(s)
        s.visited = True

        while q:
            v = q.popleft()
            res.append(v.id)
            for e in v.adj:
                w = e.dest
                if not w.visited:
                    q.append(w)
                    w.visited = True

        return res

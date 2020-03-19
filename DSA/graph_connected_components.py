class Graph:
    class Node:
        def __init__(self, val):
            self.val = val
            self.visited = false


    def __init__(self, nodes):
        self.adj_list = []
        self.cc_size = -1
        for i in range(nodes):
            self.adj_list.append([])

        
    def add_edge(self, a, b): 
        self.adj_list[a].append(b)
        self.adj_list[b].append(a)


    def connected_comps(self):
        nodes = len(self.adj_list)
        visited = [False] * nodes
        for i in range(nodes):
            if not visited[i]:
                self.dfs(i, visited)
                # print("")


    def dfs(self, v, visited): 
        visited[v] = True
        #print(v, end=' ')
        self.cc_size += 1
        for i in self.adj_list[v]: 
            if not visited[i]:
                self.dfs(i, visited)

    def bfs(self): 
        for i in range(1, 5):
            direct_friends = len(self.adj_list[i])
            print(self.cc_size - direct_friends - 1, end= ' ')


g = Graph(5)
g.add_edge(2, 1)
g.add_edge(1, 3)
g.add_edge(3, 2)
g.add_edge(3, 4)
g.connected_comps()
g.bfs()

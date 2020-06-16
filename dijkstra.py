#Dijkstra

import collections


class Graph1:
    def __init__(self):
        self.adjacency_list = {}

    @staticmethod
    def do_graph_thingies():
        graph_num = 2
        g = Graph1.create_graph(graph_num)
        g.print_graph()

        recursive = True

        g.dfs_traversal("b", recursive)
        g.dfs_traversal("c", recursive)

        g.dfs_traversal("a", recursive)
        g.dfs_traversal("a", not recursive)

        g.bfs_traversal("a")

    @staticmethod
    def create_graph(graph_num):
        g = Graph1()
        if graph_num == 1:
            g.add_edge("a", "b")
            g.add_edge("b", "c")
            g.add_edge("b", "d")
            g.add_edge("d", "c")
            g.add_edge("d", "c")
            g.add_edge("c", "a")
        elif graph_num == 2:
            g.add_edge("a", "b")
            g.add_edge("b", "c")
            g.add_edge("c", "d")
            g.add_edge("d", "d1")
            g.add_edge("d1", "d2")
            g.add_edge("c", "c1")
            g.add_edge("c1", "c2")
        elif graph_num == 3:
            g.add_edge("a", "b")
            g.add_edge("a", "c")
            g.add_edge("b", "d")
            g.add_edge("b", "e")
            g.add_edge("c", "f")
            g.add_edge("c", "g")
            g.add_edge("d", "h")
            g.add_edge("d", "i")
        else:
            g.add_edge("a", "b")
            g.add_edge("a", "c")

        return g

    def add_edge(self, v1, v2):
        if v1 not in self.adjacency_list:
            self.adjacency_list[v1] = {}
        self.adjacency_list[v1][v2] = v2

    def dfs_traversal(self, starting_vertex, recursive):
        print("DFS " + "recursive:" + str(recursive) + " starting at vertex: " + str(starting_vertex) + ":")

        visited = {}

        if recursive:
            self.dfs(starting_vertex, visited)
        else:
            self.dfs_non_recursive(starting_vertex, visited)

        print("")

    def visit_vertex(self, v, visited):
        visited[v] = True
        print(str(v) + " ")

    def dfs_non_recursive(self, v, visited):
        s = collections.deque()
        s.append(v)

        while s:
            vertex = s.pop()
            self.visit_vertex(vertex, visited)

            self.push_unvisited_neighbors(vertex, s, visited)

    def push_unvisited_neighbors(self, vertex, s, visited):
        # If vertex has no neighbors, nothing to do
        if vertex not in self.adjacency_list:
            return

        neighbors = self.adjacency_list[vertex]

        for neighbor_vertex in neighbors:
            if neighbor_vertex not in visited or visited[neighbor_vertex] is False:
                s.append(neighbor_vertex)

    def push_unvisited_neighors_maintain_dfs_recusrive_order(self, vertex, s, visited):
        # If vertex has no neighbors, nothing to do
        if vertex not in self.adjacency_list:
            return

        neighbors = self.adjacency_list[vertex]

        s2 = collections.deque()

        for neighbor_vertex in neighbors:
            if neighbor_vertex not in visited or visited[neighbor_vertex] is False:
                s2.append(neighbor_vertex)

        for vtx in s2:
            s.append(vtx)

    def dfs(self, v, visited):
        self.visit_vertex(v, visited)

        # If v has no neighbors, nothing more to do
        if v not in self.adjacency_list:
            return

        neighbors = self.adjacency_list[v]
        for neighbor_vertex in neighbors:
            if neighbor_vertex not in visited or visited[neighbor_vertex] is False:
                self.dfs(neighbor_vertex, visited)

    def bfs_traversal(self, starting_vertex):
        print ("bfs starting at vertex " + str(starting_vertex) + ":")
        visited = {}
        self.bfs(starting_vertex, visited)
        print("")

    def bfs(self, v, visited):
        q = collections.deque()
        q.appendleft(v)

        while q:
            vertex = q.pop()
            self.visit_vertex(vertex, visited)

            self.enqueue_unvisited_neighbors(vertex, q, visited)

    def enqueue_unvisited_neighbors(self, vertex, q, visited):
        # If v has no neighbors, nothing to do
        if vertex not in self.adjacency_list:
            return

        neighbors = self.adjacency_list[vertex]
        for neighbor_vertex in neighbors:
            if neighbor_vertex not in visited or visited[neighbor_vertex] is False:
                q.appendleft(neighbor_vertex)

    def print_graph(self):
        for entry in self.adjacency_list:
            vertex_neighbors = self.adjacency_list[entry]
            print(str(entry) + ": ")
            self.print_vertices(vertex_neighbors)
            print()

    def print_vertices(self, vertices):
        for entry in vertices:
            print(str(vertices[entry]) + " ")







Graph1.do_graph_thingies()

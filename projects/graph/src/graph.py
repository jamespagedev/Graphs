"""
Simple graph implementation
"""
#=============================================================================
""" BFS pseudocode (From Project Objectives)
BFS(graph, startVert):
    for v of graph.vertexes:
        v.color = white

    startVert.color = gray
    queue.enqueue(startVert)

    while !queue.isEmpty():
        u = queue[0]  // Peek at head of queue, but do not dequeue!

        for v of u.neighbors:
            if v.color == white:
                v.color = gray
                queue.enqueue(v)

        queue.dequeue()
        u.color = black
"""
#-----------------------------------------------------------------------------
""" DFS Recursion pseudocode (From Project Objectives)
explore(graph) {
    visit(this_vert);
    explore(remaining_graph);
}
"""

""" DFS pseudocode (From Project Objectives)
DFS(graph):
    for v of graph.verts:
        v.color = white
        v.parent = null

    for v of graph.verts:
        if v.color == white:
            DFS_visit(v)

DFS_visit(v):
    v.color = gray

    for neighbor of v.adjacent_nodes:
        if neighbor.color == white:
            neighbor.parent = v
            DFS_visit(neighbor)

    v.color = black
"""
#=============================================================================
""" BFT Psudocode (From Guided Project)
# Implement the queue, and enque the starting Vertex ID
	def bft(self, starting_vertex_id, target_id):
# Create and empty queue
		q = Queue()
		q.enqueue(starting_vertex_id)
# Create a set to store vertices
		visited = set()
# While the queue is not empty"
		while q.size() > 0:
	# Dequeue the first vertex
			v = q.dequeu()
	# If that vertex has not been visited:
		# Mark it as visited
			print(v)
			visited.add(v)
		# Add all of its neighbors to the back of the queue
			for next_vert in self.vertices[v]:
				q.enqueue(next_vert)
"""
#-----------------------------------------------------------------------------
""" DFT Psudocode (From Guided Project)
	def dft(self, starting_vertex_id):
# Create an empty stack
		s = Stack()
		s.push(starting_vertex_id)
# Create a set to store vertices
		visited = set()
# While the stack is not empty"
		while s.size() > 0:
	# Pop the first vertex
			v = s.pop()
	# If that vertex has not been visited:
		# Mark it as visited
			print(v)
			visited.add(v)
		# Add all of its neighbors to the top of the stack
			for next_vert in self.vertices[v]:
				s.push(next_vert)

#BFS returning shortest path:
	# Instead of storing each vertex in the queue, store the PATH to that vertex
	# When you dequeue, look at the last node
	# When you enqueue, copy the path and append the neighbor node and enqueue the new path
"""
#=============================================================================
from queue import Queue
from stack import Stack

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    # Part 1
    def __init__(self, vertices={}):
        self.vertices = vertices

    def add_vertex(self, verNum):
        self.vertices[verNum] = set()

    def add_directed_edge(self, verNum, edgeNum):
        if verNum not in self.vertices: # Stretch, O(1)
            raise ValueError("No %s vertex" % (verNum))
        elif edgeNum not in self.vertices: # Stretch, O(1)
            raise ValueError("No %s vertex" % (edgeNum))
        self.vertices[verNum].add(edgeNum)

    def add_bidirected_edge(self, ver1, ver2):
        if ver1 not in self.vertices: # Stretch, O(1)
            raise ValueError("No %s vertex" % (ver1))
        elif ver2 not in self.vertices: # Stretch, O(1)
            raise ValueError("No %s vertex" % (ver2))
        self.vertices[ver1].add(ver2)
        self.vertices[ver2].add(ver1)

    # Part 2
    def bft_queue(self, startVer):
        q = Queue()
        q.enqueue(startVer)

        visited = set()

        while q.len() > 0:
            vert = q.dequeue()

            if vert not in visited:
                visited.add(vert)
                for next_vert in self.vertices[vert]:
                    q.enqueue(next_vert)

    # Part 3
    def dft_stack(self, startVer):
        s = Stack()
        s.push(startVer)

        visited = set()

        while s.len() > 0:
            vert = s.pop()

            if vert not in visited:
                visited.add(vert)
                for next_vert in self.vertices[vert]:
                    s.push(next_vert)

    # Part 3.5
    def dft_recursion(self, starting_vert, visited=set()):
        # No instruction given
        visited.add(starting_vert)

        for neighbor in self.vertices[starting_vert]:
            if neighbor not in visited:
                return self.dft_recursion(neighbor, visited)

    # Part 4
    def bfs(self, graph, startVert):
        for v of graph.vertexes:
            v.color = 'white'

        startVert.color = 'gray'
        queue.enqueue(startVert)

        while queue.len() > 0:
            u = queue[0]  # Peek at head of queue, but do not dequeue!

            for v of u.neighbors:
                if v.color == 'white':
                    v.color = 'gray'
                    queue.enqueue(v)

            queue.dequeue()
            u.color = 'black'

    # Part 5
    def dfs(graph):
        for v of graph.verts:
            v.color = 'white'
            v.parent = None

        for v of graph.verts:
            if v.color == 'white':
                dfs_visit(v)

    def dfs_visit(v):
        v.color = 'gray'

        for neighbor of v.adjacent_nodes:
            if neighbor.color == 'white':
                neighbor.parent = v
                dfs_visit(neighbor)

        v.color = 'black'
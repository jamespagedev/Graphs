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

    def add_edge(self, ver1, ver2):
        if ver1 not in self.vertices: # Stretch, O(1)
            raise ValueError("No %s vertex" % (ver1))
        elif ver2 not in self.vertices: # Stretch, O(1)
            raise ValueError("No %s vertex" % (ver2))
        self.vertices[ver1].add(ver2)
        self.vertices[ver2].add(ver1)

    def add_directed_edge(self, verNum, edgeNum):
        if verNum not in self.vertices: # Stretch, O(1)
            raise ValueError("No %s vertex" % (verNum))
        elif edgeNum not in self.vertices: # Stretch, O(1)
            raise ValueError("No %s vertex" % (edgeNum))
        self.vertices[verNum].add(edgeNum)

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
    def dft_recursion(self, vert, visited=set()):
        # No instruction given
        visited.add(vert)

        for neighbor_vert in self.vertices[vert]:
            if neighbor_vert not in visited:
                self.dft_recursion(neighbor_vert, visited)

        return visited

    # Part 4
    def bfs(self, starting_vert_id, target_vert):
        # Instructions from Q&A...
        # create empty queue
        q = Queue()
        # create a visited set
        visited = set()
        # enqueue [A PATH TO] the starting vertex to the queue
        q.enqueue([starting_vert_id])
        # while the queue is not empty...
        while q.len() > 0:
            # dequeue the first [PATH] from the queue
            q_in_check = q.dequeue()
            # pull the last vertex from the path
            # check if it's visited...
            if q_in_check[-1] not in visited:
                # mark it as visited
                visited.add(q_in_check[-1])
                # check if it's equal to the target vertex, if so return the path
                if q_in_check[-1] == target_vert:
                    return q_in_check
                # put [A PATH TO] all of its neighbors in the back of the queue
                for neighbor_vert in self.vertices[q_in_check[-1]]:
                    # copy the path
                    path = q_in_check
                    # append the neighbor vertex to the path
                    path.append(neighbor_vert)
                    # enqueue the new path
                    q.enqueue(path)

        return f"vert {target_vert} not found in graph"

    # Part 5
    def dfs(self, starting_vert_id, target_vert):
        # Instructions from Q&A (DFS is same as BFS, but replace queue with stack)...
            # Note: Guranteed to give you a working path (if exist), but not the shortest path
        # create empty stack
        s = Stack()
        # create a visited set
        visited = set()
        # push [A PATH TO] the starting vertex to the stack
        s.push([starting_vert_id])
        # while the stack is not empty...
        while s.len() > 0:
            # pop the last [PATH] from the stack
            s_in_check = s.pop()
            # pull the last vertex from the path
            # check if it's visited...
            if s_in_check[-1] not in visited:
                # mark it as visited
                visited.add(s_in_check[-1])
                # check if it's equal to the target vertex, if so return the path
                if s_in_check[-1] == target_vert:
                    return s_in_check
                # put [A PATH TO] all of its neighbors in the back of the stack
                for neighbor_vert in self.vertices[s_in_check[-1]]:
                    # copy the path
                    path = s_in_check
                    # append the neighbor vertex to the path
                    path.append(neighbor_vert)
                    # enqueue the new path
                    s.push(path)

        return f"vert {target_vert} not found in graph"
import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def dft_r(self, start_vert, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vert)
        print(start_vert)
        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                self.dft_r(child_vert, visited)

    def bfs_path(self, starting_vertex_id, target_value):
        q = Queue()
        q.enqueue([starting_vertex_id])
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                visited.add(v)
                if v == target_value:
                    return path
                visited.add(v)
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)
        return None

    def dfs_r_path(self, start_vert, target_value, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add([start_vert])
        path += [start_vert]
        if start_vert == target_value:
            return path
        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                new_path = self.dfs_r_path(child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None

# Social Network

class SocialGraph:
    def __init__(self, lastID=0, users={}, friendships={}):
        self.lastID = lastID
        self.users = users
        self.friendships = friendships

    def addUser(self, name):
        pass

    def addFriendship(self, friendship_one, friendship_two):
        pass

    def populateGraph(self, num_users, avg_friendships):
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(0, num_users):
            self.addUser(f"User {i}")
        # Create Friendships:

        # Generate all possible friendship combinations
        possibleFriendships = []
        # Avoid duplicates by ensuring the first number is smaller than the second
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))
        # Shuffle the possible friendships
        random.shuffle(possibleFriendships)
        # Create friendships for the first X pairs of the list
	    # X is determined by the formula: numUsers * avgFriendships // 2
        # Need to divide by 2 since each addFriendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])
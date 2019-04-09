import random
from queue import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        for user in range(num_users):
            self.add_user("User %s" % user) # "User 0", "User 1", "User 2"...

        # Create friendships
        possible_friendships = []

        # Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle the possible friendships
        random.shuffle(possible_friendships)

        # Create friendships for the first tuple(2) of the list
	    # Tuple(2) is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range((num_users * avg_friendships) // 2):
            friendship = possible_friendships[i] # Tuple(2)
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        pass

        # !!!! IMPLEMENT ME
        # for u_id in range(user_id, self.friendships)

"""
    def get_all_social_paths(self, user_id):
        \"""
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        \"""

        # !!!! IMPLEMENT ME
        # create empty queue
        q = Queue()
        # create a visited set
        visited = {}  # Note that this is a dictionary, not a set
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
                    path = q_in_check[:] # by value, not be reference
                    # append the neighbor vertex to the path
                    path.append(neighbor_vert)
                    # enqueue the new path
                    q.enqueue(path)
        return visited
"""

# if __name__ == '__main__':
#     sg = SocialGraph()
#     sg.populate_graph(10, 2)
#     print(sg.friendships)
#     connections = sg.get_all_social_paths(1) # something like {0: set([1,2]), 1: set([0, 4])... 9: set([3,6])} random every time
#     print(connections)

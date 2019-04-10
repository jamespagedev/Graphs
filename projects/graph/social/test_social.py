#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

import unittest
from social import SocialGraph

class SocialGraphTests(unittest.TestCase):
    def setUp(self):
        self.sg = SocialGraph()  # Instantiate your graph

    # Part 1
    def test_get_all_social_paths(self):
        # example with given sg.populate_graph(10, 2)
        self.sg.friendships = {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
        self.assertEqual(self.sg.get_all_social_paths(1), {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]})

if __name__ == '__main__':
    unittest.main()

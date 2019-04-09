#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

import unittest
from graph import Graph

class GraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()  # Instantiate your graph

    def test_graph(self):
        self.graph.add_vertex('1')
        self.graph.add_vertex('2')
        self.graph.add_vertex('3')
        self.graph.add_vertex('4')
        self.graph.add_vertex('5')
        self.graph.add_vertex('6')
        self.graph.add_vertex('7')
        self.graph.add_directed_edge('5', '3')
        self.graph.add_directed_edge('6', '3')
        self.graph.add_directed_edge('7', '1')
        self.graph.add_directed_edge('4', '7')
        self.graph.add_directed_edge('1', '2')
        self.graph.add_directed_edge('7', '6')
        self.graph.add_directed_edge('2', '4')
        self.graph.add_directed_edge('3', '5')
        self.graph.add_directed_edge('2', '3')
        self.graph.add_directed_edge('4', '6')
        self.assertEqual(self.graph.vertices, {'1': set(['2']), '3': set(['5']), '2': set(['3', '4']), '5': set(['3']), '4': set(['7', '6']), '7': set(['1', '6']), '6': set(['3'])})

    def test_bfs_graph(self):
        self.graph.add_vertex('1')
        self.graph.add_vertex('2')
        self.graph.add_vertex('3')
        self.graph.add_vertex('4')
        self.graph.add_vertex('5')
        self.graph.add_vertex('6')
        self.graph.add_vertex('7')
        self.graph.add_directed_edge('1', '2')
        self.graph.add_directed_edge('2', '3')
        self.graph.add_directed_edge('2', '4')
        self.graph.add_edge('3', '5')
        self.graph.add_directed_edge('4', '6')
        self.graph.add_directed_edge('4', '7')
        self.graph.add_directed_edge('6', '3')
        self.graph.add_directed_edge('7', '1')
        self.graph.add_directed_edge('7', '6')
        self.assertEqual(self.graph.vertices, {'1': set(['2']), '3': set(['5']), '2': set(['3', '4']), '5': set(['3']), '4': set(['7', '6']), '7': set(['1', '6']), '6': set(['3'])})

if __name__ == '__main__':
    unittest.main()

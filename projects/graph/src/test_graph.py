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

    def test_bfs(self):
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
        print("bfs = %s" % (self.graph.bfs('1', '6'))) # should be ['1', '2', '4', '6']

    def test_dfs_graph(self):
        self.graph.add_vertex('1')
        self.graph.add_vertex('2')
        self.graph.add_vertex('3')
        self.graph.add_vertex('4')
        self.graph.add_vertex('5')
        self.graph.add_vertex('6')
        self.graph.add_vertex('7')
        self.graph.add_directed_edge('1', '2')
        self.graph.add_directed_edge('2', '3')
        self.graph.add_directed_edge('2', '5')
        self.graph.add_edge('3', '4')
        self.graph.add_directed_edge('5', '6')
        self.graph.add_directed_edge('5', '7')
        self.graph.add_directed_edge('6', '3')
        self.graph.add_directed_edge('7', '1')
        self.graph.add_directed_edge('7', '6')
        self.assertEqual(self.graph.vertices, {'1': set(['2']), '3': set(['4']), '2': set(['3', '5']), '5': set(['7', '6']), '4': set(['3']), '7': set(['1', '6']), '6': set(['3'])})

    def test_dfs(self):
        self.graph.add_vertex('1')
        self.graph.add_vertex('2')
        self.graph.add_vertex('3')
        self.graph.add_vertex('4')
        self.graph.add_vertex('5')
        self.graph.add_vertex('6')
        self.graph.add_vertex('7')
        self.graph.add_directed_edge('1', '2')
        self.graph.add_directed_edge('2', '3')
        self.graph.add_directed_edge('2', '5')
        self.graph.add_edge('3', '4')
        self.graph.add_directed_edge('5', '6')
        self.graph.add_directed_edge('5', '7')
        self.graph.add_directed_edge('6', '3')
        self.graph.add_directed_edge('7', '1')
        self.graph.add_directed_edge('7', '6')
        print("dfs = %s" % (self.graph.dfs('1', '6'))) # not sure about random path... but shouldn't include vertexes out of path

if __name__ == '__main__':
    unittest.main()

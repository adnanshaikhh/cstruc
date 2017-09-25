'''Defines graph structure'''

import os
import random

class Graph:
    '''
    Store edges and nodes
    '''

    def __init__(self):
        self.edges = []
        self.nodes = {}
        self.group_granularity = 2
   
    def add(self, node_name, neighbours):
        node = self._get_or_add_node(node_name)

        for neighbour_name in neighbours:
            neighbor = self._get_or_add_node(neighbour_name)
            neighbor['size'] += 1
            self._add_edge(node, neighbor)

    def to_json(self):
        nodes = list(self.nodes.values())
        return dict(nodes=nodes, edges=self.edges)

    def is_empty(self):
        return len(self.nodes) == 0

    def _get_or_add_node(self, node_name):
        node = self.nodes.get(node_name)
        if node is None:
            node = self._add_node(node_name)
        return node

    def _add_node(self, node_name):
        node = {}
        node['id'] = len(self.nodes)
        node['size'] = 1
        node['color'] = "rgba(256,31,55,0.7)"
        node['label'] = os.path.basename(node_name)

        directories = os.path.dirname(node_name).split(os.sep)
        begin = len(directories) - self.group_granularity
        node['group'] = os.sep.join(directories[begin:begin + 2])

        node['x'] = random.random() * 0.01
        node['y'] = random.random() * 0.01

        self.nodes[node_name] = node

        return node

    def _add_edge(self, source_node, target_node):
        edge = {}
        edge['id'] = len(self.edges)
        edge['size'] = 10
        edge['type'] = 'curvedArrow'

        source_node, target_node = target_node, source_node
        
        edge['source'] = source_node['id']
        edge['target'] = target_node['id']

        self.edges.append(edge)

        return edge

    def __repr__(self):
        num_nodes = len(self.nodes)
        num_edges = len(self.edges)
        return "<Graph: nodes = " + str(num_nodes) + ", edges = " + str(num_edges) + ">"

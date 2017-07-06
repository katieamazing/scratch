"""
Ch. 4.1: Route Between Nodes
Given a directed graph, design an algorithm to find out whether there is a route
between nodes.
"""
dg = {} # a directed graph

def is_path(graph, starting_node, ending_node):
    starting_node.visited = True
    for n in starting_node.neighbor:
        if n == ending_node:
            return True
        if not n.visited:
            if is_path(graph, neighbor, ending_node):
                return True
    return False

"""
Ch. 4.4: Check Balanced
Implement a function to check if a binary tree is balanced.
For this question, a balanced tree is defined as a tree where the heights of the
two subtrees of any node never differ by more than one.
"""

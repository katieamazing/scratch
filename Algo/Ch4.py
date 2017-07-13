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

def is_path(graph, starting_node, ending_node):
    q = [starting_node]
    while True:
        if q == []:
            return False
        focus = q.pop()
        focus.visited = True
        for n in focus.neighbor:
            if not n.visited:
                q.append(focus, 0)
            if n == ending_node:
                return True

"""
Ch. 4.4: Check Balanced
Implement a function to check if a binary tree is balanced.
For this question, a balanced tree is defined as a tree where the heights of the
two subtrees of any node never differ by more than one.
"""

def check_balanced(root):
    if not root:
        return (0, True)
    else:
        lh, lb = check_balanced(root.left)
        rh, rb = check_balanced(root.right)
        return (max(lh, rh) + 1, False)

"""
    go to deepest left leaf

    record the depth

    go down to that depth on other paths

    check each leaf for either
        having a parent one depth up
        or having child/children max one depth down
"""

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

# figure out if a tree is a BST
def is_bst(n):
    left_result = True
    right_result = True

    if n.left:
        if n.left.val > n.val:
            return False
        else:
            left_result = is_bst(n.left)

    if n.right:
        if n.right.val < n.val:
            return False
        else:
            right_result = is_bst(n.right)

    return (right_result and left_result)


def is_bst_but_pretty(n): #always pattern for consuming a tree as input
    if not n: #base case, at a leaf
        return True
    else:
        left_result = is_bst_but_pretty(n.left)
        right_result = is_bst_but_pretty(n.right)

        return (n.left.val < n.val and n.right.val > n.val and left_result and right_result)


def count_nodes(n): #always pattern for consuming a tree as input
    if not n: #base case, at a leaf
        return 0
    else:
        return = 1 + count_nodes(n.left) + count_nodes(n.right)


def actually_a_bst(n): #helper function pattern for consuming a tree input

    def inner(n, min, max):
        if not n:
            return False
        else:
            left = inner(n.left, min, n.val)
            right = inner(n.right, n.val, max)
            node_left = n.left and n.left.val < n.val
            node_right = n.right and n.right.val > n.val
            return (left and right and node_left and node_right)

    return inner(n, -infinity, infinity)





#ask honjicholas to teach you this OOP style






















    .

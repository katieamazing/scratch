class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def second_largest(root):
    if not root or (not root.left and not root.right):
        raise Exception("Tree must have at least two nodes")

    if root.left and not root.right:
        return second_largest(root.left)

    if root.right and not not root.right.left and not root.right.right:
        return root.value

    return second_largest(root.right)

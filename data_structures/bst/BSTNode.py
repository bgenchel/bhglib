"""
Node object for a BST
"""


class BSTNode:
    left = None
    right = None
    parent = None
    height = 0
    priority = -1
    data = None

    def __init__(self, data):
        self.data = data
        return

    def update_height(self):
        if self.left is None:
            leftHeight = -1
        else:
            leftHeight = self.left.height

        if self.right is None:
            rightHeight = -1
        else:
            rightHeight = self.right.height

        self.height = max(leftHeight, rightHeight) + 1
        return

    def balance(self):
        if self.left is None:
            leftHeight = -1
        else:
            leftHeight = self.left.height

        if self.right is None:
            rightHeight = -1
        else:
            rightHeight = self.right.height

        return leftHeight - rightHeight

    def successor(self):
        """
        Return the inorder successor to the current node.
        Algorithm: If a right subtree exists, go right, then left as much as possible.
        else, go to parent. If parent is a left child, then its parent is the successor.
        If the parent is a right child, keep going until you find a left child. If you
        never do, return None
        """
        curr = self
        if curr.right is not None:
            curr = curr.right
            while curr.left is not None:
                curr = curr.left
            return curr
        else:
            while curr.parent is not None:
                if curr.parent.left == curr:
                    return curr.parent
                else:
                    curr = curr.parent
        return None


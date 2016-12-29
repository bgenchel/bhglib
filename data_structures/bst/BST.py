"""
Python implementation of a self balancing (AVL) Binary Search Tree,
borrows many conventions from the C++ code it was adapted from.

TODO:
    fix self balancing,
    fix delete root. 
"""

from BSTNode import BSTNode
from BSTIterator import BSTIterator


class BST(object):
    root = None
    size = 0

# PUBLIC

    def __init__(self):
        return

    def __len__(self):
        return self.size

    def insert(self, item):
        if self.empty():
            self.root = BSTNode(item)
            self.size += 1
            return True

        if self._insert_recurse(self.root, item):
            self.size += 1
            return True
        else:
            return False

    def _insert_recurse(self, curr, item):
        if item < curr.data:
            if curr.left is not None:
                if not self._insert_recurse(curr.left, item):
                    return False
            else:
                curr.left = BSTNode(item)
                curr.left.parent = curr
        elif curr.data < item:
            if curr.right is not None:
                if not self._insert_recurse(curr.right, item):
                    return False
            else:
                curr.right = BSTNode(item)
                curr.right.parent = curr
        else:
            return False  # already in tree

        curr.update_height()
        if curr.balance() > 1:
            self._rotate_right(curr)
        elif curr.balance() < -1:
            self._rotate_left(curr)

        return True

    def find(self, item):
        """
        search for an element in the tree, return an iterator to
        that element if found. otherwise, return an iterator pointing past
        the last item in the BST
        """
        current = self.root
        while current is not None:
            if item < current.data:
                current = current.left
            elif current.data < item:
                current = current.right
            else:
                return BSTIterator(current)
        return self.end()

    def delete(self, item):
        if self.root is None:
            return False
        else:
            return self._delete_recurse(self.root, item)

    def _delete_recurse(self, curr, item):
        if item < curr.data:
            if curr.left is not None:
                return self._delete_recurse(curr.left, item)
            else:
                return False
        elif curr.data < item:
            if curr.right is not None:
                return self._delete_recurse(curr.right, item)
            else:
                return False
        else:
            if curr.left is not None and curr.right is not None:
                toswitch = self._first(curr.right)
                curr.data = toswitch.data
                curr = toswitch
            else:
                if curr.left is None and curr.right is None:
                    replace = None
                elif curr.left is not None and curr.right is None:
                    replace = curr.left
                elif curr.right is not None and curr.left is None:
                    replace = curr.right

                if curr.parent and curr.parent.right == curr:
                    curr.parent.right = replace
                elif curr.parent and curr.parent.left == curr:
                    curr.parent.left = replace

            del curr
            self.size -= 1
            return True

    def inorder(self):
        self._inorder(self.root)

    def empty(self):
        """
        return True if BST is empty, else false
        """
        return self.root is None

    def begin(self):
        """
        return an iterator to the first item in the BST
        """
        return BSTIterator(self._first(self.root))

    def end(self):
        """
        return an iterator pointing past the last item in the BST
        """
        return BSTIterator(None)

    # PRIVATE
    def _rotate_right(self, node):
        """
        balance the tree by rotating right at a given node
        """
        par = node
        child = node.left

        if(self.root == par):
            self.root = child
            child.parent = None
        elif par.parent.right == par:
            par.parent.right = child
            child.parent = par.parent
        elif par.parent.left == par:
            par.parent.left = child
            child.parent = par.parent

        par.left = child.right
        if par.left is not None:
            par.left.parent = par

        child.right = par
        par.parent = child
        child.update_height()
        par.update_height()
        return

    def _rotate_left(self, node):
        par = node
        child = node.right

        if self.root == par:
            self.root = child
            child.parent = None
        elif par.parent.right == par:
            par.parent.right = child
            child.parent = par.parent
        elif par.parent.left == par:
            par.parent.left = child
            child.parent = par.parent

        par.right = child.left
        if par.right is not None:
            par.right.parent = par

        child.left = par
        par.parent = child
        child.update_height()
        par.update_height()
        return

    def _height(self, node):
        if node is None:
            return 0
        else:
            return max(self._height(node.left), self._height(node.right)) + 1

    def _subtree_size(self, node):
        """
        return the size of a subtree with root at the node passed in
        """
        if node is None:
            return 0
        else:
            return 1 + self._subtree_size(node.left) + self._subtree_size(node.right)

    def _inorder(self, node):
        """
        prints a subtree with root at the node passed in
        """
        if node is None:
            return

        self._inorder(node.left)
        print node.data
        self._inorder(node.right)

    def _first(self, node):
        """
        returns the first node in the ordered set of nodes
        """
        if node is None:
            return None
        assert isinstance(node, BSTNode)
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr








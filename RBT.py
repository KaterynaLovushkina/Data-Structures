from enum import Enum


class Color(Enum):
    BLACK="Black"
    RED="Red"

class RBNode(object):
    def __init__(self, data, parent=None, color = Color.RED):
        self.color = color
        self.parent = parent
        self.data = data
        self.left = None
        self.right = None


class RedBlackTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = RBNode(val, color=Color.BLACK)

        else:
            self._insert(val, self.root)

    def _insert(self, val, curr_node):
        if curr_node is None:
            return None

        if val < curr_node.data:
            # node.left is not None
            if curr_node.left:
                self._insert(val, curr_node.left)
            # node.left is None, insert
            else:
                curr_node.left = RBNode(val, parent=curr_node)
                self.fix_tree_after_add(curr_node.left)
        else:
            # node.right is not None
            if curr_node.right:
                self._insert(val, curr_node.right)
            # node.right is None, insert
            else:
                curr_node.right = RBNode(val, parent=curr_node)
                self.fix_tree_after_add(curr_node.right)

    def fix_tree_after_add(self, new_node):
        while  new_node.parent and new_node.parent.color == Color.RED:
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right

                if uncle and  uncle.color == Color.RED:
                        # This is Case 1
                        new_node.parent.color = Color.BLACK
                        uncle.color = Color.BLACK
                        new_node.parent.parent.color = Color.RED
                        new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        # This is Case 2
                        new_node = new_node.parent
                        self.left_rotate(new_node)
                    # This is Case 3
                    new_node.parent.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    self.right_rotate(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.left
                if uncle and uncle.color == Color.RED:
                        # Case 1
                    new_node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        # Case 2
                        new_node = new_node.parent
                        self.right_rotate(new_node)
                    # Case 3
                    new_node.parent.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    self.left_rotate(new_node.parent.parent)
        self.root.color = Color.BLACK

    def left_rotate(self, node):
        right_sub_tree = node.right
        node.right = right_sub_tree.left
        if right_sub_tree.left:
            right_sub_tree.left.parent = node

        right_sub_tree.parent = node.parent
        if node.parent is None:
            self.root = right_sub_tree
        else:
            if node == node.parent.left:
                node.parent.left = right_sub_tree
            else:
                node.parent.right = right_sub_tree
        right_sub_tree.left = node
        node.parent = right_sub_tree

    def right_rotate(self, node):
        left_sub_tree = node.left
        node.left = left_sub_tree.right
        if left_sub_tree.right:
            left_sub_tree.right.parent = node

        left_sub_tree.parent = node.parent
        if node.parent == None:
            self.root = left_sub_tree
        else:
            if node == node.parent.right:
                node.parent.right = left_sub_tree
            else:
                node.parent.left = left_sub_tree
        left_sub_tree.right = node
        node.parent = left_sub_tree

    def printTree(self):
        if self.root is None:
            return
        else:
            self._printTree(self.root)

    def _printTree(self, node, level=0):
        if node:
            self._printTree(node.right, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.data) +"  " + str(node.color.value))
            self._printTree(node.left, level + 1)

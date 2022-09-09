class AVLNode:  # node class hidden from client
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


class AVLTree:

    def __init__(self):
        self.root = None

    def insertNode(self, value):
        self.root = self._insertNode(self.root, value)

    def _insertNode(self, node, value):  # recursive _put follow tree down till place found for new node
        if not node:  # place found, return new node
            return AVLNode(value)

        elif value < node.value:
            node.left = self._insertNode(node.left, value)
        elif value > node.value:
            node.right = self._insertNode(node.right, value)
        else:  # equal
            node.value = value  # key already in tree, change value
            return node  # return existing node
        return self.makeTreeBalanced(node)

    def makeTreeBalanced(self, node):
        node.height = 1 + max(self._getHeight(node.right), self._getHeight(node.left))
        balance = self._getBalance(node)

        # check for imbalance and rotate to correct
        if balance > 1:  # left heavy
            if self._getBalance(node.left) < 0:
                node.left = self._leftRotate(node.left)  # Left Right
            return self._rightRotate(node)  # catch either Left Right or Right Right
        elif balance < -1:
            if self._getBalance(node.right) > 0:
                node.right = self._rightRotate(node.right)  # Right Left
            return self._leftRotate(node)  # catch either Right Left or Left Left

        return node

    def deleteNode(self, value):
        self.root = self._deleteNode(self.root, value)

    # Recursive function to delete a node with given key from subtree with given node.
    # It returns node of the modified subtree.
    def _deleteNode(self, node, value):
        if not node:
            return node  # not found

        # find node with key
        elif value < node.value:
            node.left = self._deleteNode(node.left, value)
        elif value > node.value:
            node.right = self._deleteNode(node.right, value)
        else:  # equal, it is found
            if node.left is None:  # case of only right child
                return node.right  # replace node with child

            elif node.right is None:  # case of only left child
                return node.left  # replace node with child

            # case of two children
            current_node = node.right
            while current_node.left:
                current_node = current_node.left
            node.value = current_node.value
            node.right = self._deleteNode(node.right, node.value)

        # If the tree has only one node, simply return it

        return self.makeTreeBalanced(node)

    def getHeight(self):
        return self._getHeight(self.root)

    def _getHeight(self, node):
        return node.height if node else -1

    def getBalance(self):
        return self._getBalance(self.root)

    def _getBalance(self, node):
        return self._getHeight(node.left) - self._getHeight(node.right)

    def _leftRotate(self, node):  # a                    b
        root = node.right
        temp = root.left

        root.left = node
        node.right = temp

        node.height = max(self._getHeight(node.left), self._getHeight(node.right)) + 1
        root.height = max(self._getHeight(root.left), self._getHeight(root.right)) + 1
        return root

    def _rightRotate(self, node):  # a                b
        root = node.left  # /    Right       / \\  < update link \\
        x = root.right  # b     Rotate(a)  c   a
        root.right = node  # update b right link point to a             /  \   - - ->     //      < update link //
        node.left = x  # replace c left link to now point to x      c    x            x
        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))
        root.height = 1 + max(self._getHeight(root.left), self._getHeight(node.right))
        return root


    def printTree(self):
        if self.root is None:
            return
        else:
            self._printTree(self.root)

    def _printTree(self, node, level=0):
        if node != None:
            self._printTree(node.right, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.value))
            self._printTree(node.left, level + 1)


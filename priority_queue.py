class Node:
    def __init__(self, node, weight):
        self.vertex = node
        self.weight = weight
        self.next = None

class PriorityQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, el, weight):

        if self.size == 0:
            self.head = self.tail = Node(el, weight)
        else:
            old_tail = self.tail
            old_tail.next = Node(el, weight)
            self.tail = old_tail.next
        self.size +=1

    def pop(self):
        del_node = self.head
        if self.size == 0:
            raise(IndexError('The queue dont have elements'))
        elif self.size == 1:
            self.head = self.tail = None
        else:
            self.head = del_node.next
        self.size -=1
        return del_node.vertex

    def find(self, finded_node, weight):
        node = self.head
        while node:
            if node.vertex== finded_node:
                node.weight = weight
                return True
            node = node.next
        return False
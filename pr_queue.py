class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, x, y):
        if self.size == 0:
            self.head=self.tail= Node(x,y)
        else:
            node = self.tail
            self.tail.next = Node(x,y)
            self.tail = node.next
        self.size +=1

    def pop(self):
        if self.size == 0:
            raise IndexError('OUT OF RANGE')
        else:
            node_first = self.head
            if self.size == 1:
                self.head = self.tail = None
            self.head = node_first.next
        self.size -=1
        return (node_first.x, node_first.y)

    def print(self):
        node = self.head
        while node:
            print(node.x, node.y)
            node = node.next


if __name__ == '__main__':
    queue_1 = PriorityQueue()
    queue_1.push(0,1)
    queue_1.push(0,2)
    queue_1.push(1,3)
    queue_1.push(1,4)

    queue_1.pop()
    queue_1.print()
    print(queue_1.pop())
from Plate import Plate

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def push(self, node: Plate):
        if self.size == 0:
            self.head = self.tail = node
        else:
            old_last = self.tail
            old_last.next = node
            node.parent = old_last
            self.tail =node
        self.size +=1

    def pop(self):
        old_head = self.tail
        if self.size == 0:
            raise(IndexError("The queue is empty"))
        elif self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = old_head.parent
        self.size -=1
        return old_head



if __name__ == '__main__':
    queue_1 = Stack()
    queue_1.push(Plate("a", (0, 0)))
    queue_1.push(Plate("a", (0, 1)))
    queue_1.push(Plate("a", (0, 2)))

    queue_1.pop()
    queue_1.pop()

    print(queue_1.pop())
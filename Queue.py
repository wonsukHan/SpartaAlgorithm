class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.is_empty():
            self.head = Node(data)
            self.tail = self.head
        else:
            new = Node(data)
            self.tail.next = new
            new = self.tail

    def dequeue(self):
        if self.is_empty():
            return "Stack is Empty"
        pop = self.head
        self.head = self.head.next
        return pop.data

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.head.data

    def is_empty(self):
        return self.head is None
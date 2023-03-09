class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        pop = self.head
        self.head = self.head.next
        return pop.data

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None


stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop())
print(stack.peek())


top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    rec = []
    for i in range(len(heights)):
        for j in range(i, -1, -1):
            if heights[j] > heights[i]:
                rec.append(j + 1)
                break
        if j == 0:
            rec.append(0)
    return rec


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
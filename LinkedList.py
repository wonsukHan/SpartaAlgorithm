class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur.next is not None:
            print(cur.data)
            cur = cur.next
        print(cur.data)

    def get_node(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur

    def add_node(self, index, data):
        if index == 0:
            cur = Node(data)
            cur.next = self.head
            self.head = cur
        else:
            cur = self.get_node(index - 1)
            cur_next = cur.next
            cur.next = Node(data)
            cur.next.next = cur_next

    def delete_node(self, index):
        if index == 0:
            self.head = self.get_node(1)
        else:
            cur = self.get_node(index - 1)
            cur.next = cur.next.next



linked_list = LinkedList()
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(12)
print(linked_list.get_node(2).data, '\n')
linked_list.add_node(0, 20)
linked_list.delete_node(2)
linked_list.print_all()



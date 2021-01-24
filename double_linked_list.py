class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert(self, prev_node, new_val):
        if prev_node is None:
            return

        new_node = Node(new_val)
        new_node.next = prev_node.next
        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, new_val):
        new_node = Node(new_val)

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head

        while last.next is not None:
            last = last.next

        last.next = new_node
        new_node.prev = last

        return

    def list_print(self, node):
        while node is not None:
            print(node.data)
            node = node.next


d_list = DoubleLinkedList()
d_list.add(12)
d_list.append(9)
d_list.add(8)
d_list.add(62)
d_list.append(45)

# d_list.insert(d_list.head.next, 13)

d_list.list_print(d_list.head)
class Node:
    def __init__(self, data_val):
        self.data_val = data_val
        self.next_val = None


class SLinkedList:
    def __init__(self):
        self.head_val = None

    def list_print(self):
        printval = self.head_val
        while printval is not None:
            print(printval.data_val)
            printval = printval.next_val

    def at_beginning(self, new_data):
        new_node = Node(new_data)

        new_node.next_val = self.head_val
        self.head_val = new_node

    def at_end(self, new_data):
        new_node = Node(new_data)

        if self.head_val is None:
            self.head_val = new_node
            return

        last = self.head_val

        while(last.next_val):
            last = last.next_val
        last.next_val = new_node

    def in_between(self, middle_node, new_data):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        new_node = Node(new_data)
        new_node.next_val = middle_node.next_val
        middle_node.next_val = new_node

    def remove_node(self, remove_key):
        head = self.head_val

        if head is not None:
            if head.data_val == remove_key:
                self.head_val = head.next_val
                head = None
                return

        while (head is not None):
            if head.data_val == remove_key:
                break
            prev = head
            head = head.next_val

        if head is None:
            return

        prev.next_val = head.next_val

        head = None

list1 = SLinkedList()
list1.head_val = Node("Mon")

e2 = Node("Tue")
e3 = Node("Thu")

list1.head_val.next_val = e2
e2.next_val = e3

list1.at_end("Fri")

list1.in_between(list1.head_val.next_val, "Wed")
list1.remove_node("Tue")
list1.list_print()
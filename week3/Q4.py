class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, data, position):
        if position < 0 or position > self.length():
            raise IndexError("Invalid position")

        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while count < position - 1:
                current = current.next
                count += 1
            new_node.next = current.next
            current.next = new_node

    def delete(self, data):
        if self.is_empty():
            raise Exception("List is empty")

        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                else:
                    current = current.next
            raise ValueError("Data not found in list")

    def search(self, data):
        if self.is_empty():
            raise Exception("List is empty")

        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

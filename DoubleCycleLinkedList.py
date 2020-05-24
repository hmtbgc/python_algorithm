class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return f"Node {self.data}"

class DoubleCycleLinkedList:
    def __init__(self):
        self.head = Node(63)
        self.size = 0

    def __repr__(self):
        p = self.head.next
        if (p == self.head):
            return "None"
        output = p.__repr__()
        p = p.next
        while (p != self.head):
            output = output + " -> " + p.__repr__()
            p = p.next
        return output
    
    def insert_head(self, data):
        insert_node = Node(data)
        if (self.head.next):
            self.head.next.prev = insert_node
            insert_node.next = self.head.next
            insert_node.prev = self.head
            self.head.next = insert_node
        else:
            self.head.next = insert_node
            insert_node.prev = self.head
            insert_node.next = self.head
            self.head.prev = insert_node
        self.size += 1
    
    def insert_tail(self, data):
        insert_node = Node(data)
        if (self.head.prev):
            self.head.prev.next = insert_node
            insert_node.prev = self.head.prev
            insert_node.next = self.head
            self.head.prev = insert_node
        else:
            self.head.next = insert_node
            insert_node.prev = self.head
            insert_node.next = self.head
            self.head.prev = insert_node
        self.size += 1
    
    def delete_head(self):
        p = self.head.next
        if (p == self.head):
            return "The list is empty!"
        if (not p.next):
            self.head.next = None
            self.head.prev = None
        else:
            self.head.next = p.next
            p.next.prev = self.head
        self.size -= 1
        return p

    def delete_tail(self):
        p = self.head.prev
        if (p == self.head):
            return "The list is empty!"
        if (not p.prev):
            self.head.next = None
            self.head.prev = None
        else:
            self.head.prev = p.prev
            p.prev.next = self.head
        self.size -= 1
        return p
    
    def list_size(self):
        return self.size

    def find_head(self):
        if (self.head.next == self.head):
            return None
        return self.head.next
    
    def find_tail(self):
        if (self.head.next == self.head):
            return None
        return self.head.prev
    


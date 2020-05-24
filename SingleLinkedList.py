class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node {self.data}"
    
class SingleLinkedList:
    def __init__(self):
        self.head = Node(63)
        self.size = 0

    def __repr__(self):
        p = self.head.next
        if (not p):
            return "None"
        output = p.__repr__()
        p = p.next
        while (p):
            output = output + " -> " + p.__repr__()
            p = p.next
        return output
    
    def insert_head(self, data):
        insert_node = Node(data)
        insert_node.next = self.head.next
        self.head.next = insert_node
        self.size += 1

    def find_head(self):
        return self.head.next
    
    def insert_tail(self, data):
        insert_node = Node(data)
        p = self.head
        while (p.next):
            p = p.next
        p.next = insert_node
        self.size += 1

    def find_tail(self):
        p = self.head
        while (p.next):
            p = p.next
        return p

    def delete_head(self):
        p = self.head.next
        if (not p):
            return "The list is empty!"
        else:
            self.head.next = p.next
            self.size -= 1
        return p
    
    def delete_tail(self):
        p = self.head
        if (not p.next):
            return "The list is empty!"
        else:
            while (p.next.next):
                p = p.next
            temp_Node = p.next
            p.next = None
            self.size -= 1
            return temp_Node
    
    def list_size(self):
        return self.size 
    
        
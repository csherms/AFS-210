class Node(object):
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
        
        
        
class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    
    def append(self, data):
        new_node = Node(data, None, None)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1
            
            
    def delete(self, data):
        current = self.head
        node_deleted = False
        if current is None:
                node_deleted = False
        elif current.data == data:
                self.head = current.next
                self.head.prev = None
                node_deleted = True
        elif self.tail.data == data:
                self.tail = self.tail.prev
                self.tail.next = None
                node_deleted = True
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
        if node_deleted:
            self.count -= 1
            
            
    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val
        
        
    def search(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True
            return False
            
    
    def peek(self):
        if self.head:
            return self.head.data
        if self.tail:
            return self.tail.data
        else:
            return None
        
        
        
new_list = DoublyLinkedList()
new_list.append("Hello")
new_list.append("World")
print(new_list.peek())
print(new_list.search("World"))
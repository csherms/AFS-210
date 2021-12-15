a = "eggs"
b = "ham"
c = "spam"


# This is the simplest type of node class, it only has a single node and a next pointer set to None. 
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# this is optional: this __str__ method makes it so when I print the new node the data will be printed rather than
# returning a node class
    def __str__(self):
        return str(self.data)




class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0  # Add this counter-part to append function


    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
            self.size += 1 


    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val


    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next


    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False


    def clear(self):
        self.tail = None
        self.head = None


words = SinglyLinkedList()
words.append("eggs")
words.append("ham")
words.append("spam")
print(words)
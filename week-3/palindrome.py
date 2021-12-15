class Stack:
    def __init__(self):
        self.items = []
        
        
    def push(self, item):
        self.items.insert(0, item)
        
    def pop(self):
        returned_item = self.items.pop(0)
        return returned_item
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[0]
              
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        returned_item = self.queue.pop(0)
        return returned_item
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def peek(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]
        

def is_palindrome (data):
    new_stack = Stack()
    new_queue = Queue()
    
    for ch in data:
        new_stack.push(ch)
        new_queue.enqueue(ch)
    
    while new_stack.is_empty() != True: 
        nsp = new_stack.peek()
        nqp = new_queue.peek()
        if(nsp == nqp):
            new_stack.pop()
            new_queue.dequeue()
        else: 
            return False
    return True
    
print(is_palindrome("racecar"))
print(is_palindrome("noon"))
print(is_palindrome("python"))
print(is_palindrome("madam"))

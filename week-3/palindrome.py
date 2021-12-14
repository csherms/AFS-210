class Stack:
    def __init__(self):
        self.items = []
        self.count = 0
        
        
    def push(self, item):
        self.items.insert(0, item)
        self.count += 1
        
    def pop(self):
        returned_item = self.items.pop(-1)
        self.count -= 1
        return returned_item
    
    def size(self):
        return self.count
    
    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False
    
    def peek(self):
        if self.count == 0:
            return None
        else:
            return self.items[0]
              
class Queue():
    def __init__(self):
        self.queue = []
        self.count = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.count += 1
        
    def dequeue(self):
        returned_item = self.queue.pop(0)
        self.count -= 1
        return returned_item
    
    def size(self):
        return self.count
    
    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False
    
    def peek(self):
        if self.count == 0:
            return None
        else:
            return self.queue[0]
        

def is_palindrome (data):
    new_stack = Stack()
    new_stack.push(data)
    while new_stack.items:
        answer = new_stack.items[0] == new_stack.items[0][::-1]
        new_stack.count -= 1
        if answer == True:
            return print("True")
        else:
            return print("False")
    
    new_queue = Queue()
    new_queue.enqueue(data)
    while new_queue.queue:
        answer = new_queue.queue[0] == new_queue.queue[0][::-1]
        new_queue.count -= 1
        if answer == True:
            return print("True")
        else:
            return print("False")
    
is_palindrome("racecar")
is_palindrome("noon")
is_palindrome("python")
is_palindrome("madam")

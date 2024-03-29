# class ListQueue:
#     def __init__(self):
#         self.items = []
#         self.size = 0
        
    
#     def enqueu(self, data):
#         self.items.insert(0, data)
#         self.size += 1
        
        
#     def dequeu(self):
#         data = self.items.pop()
#         self.size -= 1
#         return data


# Stack based queue with inbound and outbound stacks
# class Queue:
#     def __init__(self):
#         self.inbound_stack = []
#         self.outbound_stack = []
        
        
#     def enqueue(self, data):
#         self.inbound_stack.append(data)
        
        
#     def dequeue(self):
#         if not self.outbound_stack: 
#             while self.inbound_stack: 
#                 self.outbound_stack.append(self.inbound_stack.pop()) 
#         return self.outbound_stack.pop()

        
# queue = Queue() 
# queue.enqueue(5) 
# queue.enqueue(6) 
# queue.enqueue(7) 
# print(queue.inbound_stack) 
# queue.dequeue() 
# print(queue.inbound_stack) 
# print(queue.outbound_stack) 
# queue.dequeue() 
# print(queue.outbound_stack)



# Node based Queue
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None
        
        
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
        
    def enqueu(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1
        
        
    def dequeue(self):
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
    
    
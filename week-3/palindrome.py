class Stack:

    def __init__(self, *item):
        self.stack = []
        
    def pushit(self, item):
        if len(self.stack) == 9:
            print("Stack is full: " + self.stack)
        else:
            print(self.stack.append(self.item))
            
    def popit(self):
        if self.stack == []:
            print("Stack underflow: " + self.stack)
        else:
            print(self.stack.pop())
            
new_thing = Stack()
new_thing.pushit("Hello", "Bitch")
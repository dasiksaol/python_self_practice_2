### Exercise 5: Implement a Stack using a Python Class

# Create a Python class representing a stack data structure with push, pop, and isEmpty methods.

class Stack:
    def __init__(self):
        self.list = []
    
    def push(self, num):
        self.list.append(num)
        return self.list
    
    def pop(self):
        self.list.pop()
        return self.list

    def is_empty(self):
        self.list = []
        return self.list

stack = Stack()
print(stack.push(5))
print(stack.push(10))
print(stack.pop())
print(stack.is_empty())
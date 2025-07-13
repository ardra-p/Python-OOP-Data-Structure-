class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,elemnet):
        self.stack.append(elemnet)

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty No peek Value"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack)==0
    
    def length(self):
        return len(self.stack)
    
    def print_elements(self):
        print([x for x in self.stack])
    




class Stack:

    def __init__(self):

        self.array = []

    def peek(self):
        if len(self.array) > 0:
            lastIndex = len(self.array) - 1
            return self.array[lastIndex]

    def push(self, value):

        self.array.append(value)

    def pop(self):
        itemToPop = self.array[len(self.array) - 1]
        self.array.pop(len(self.array) - 1)
        return itemToPop
    
    
class MyQueue:

    def __init__(self):

        self.myStack = Stack()       

    def push(self, x):
        
        self.myStack.array.insert(0, x)
        

    def pop(self):
        
        self.myStack.pop()
        

    def peek(self):
        
        self.myStack.peek()
        

    def empty(self) -> bool:
        
        if len(self.myStack.array) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(13)



param_3 = obj.peek()
param_4 = obj.empty()

print(param_3)
print(param_4)
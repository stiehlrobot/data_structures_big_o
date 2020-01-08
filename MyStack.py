class Node:

    def __init__(self, value):
        self.value = value
        self.next = None



class Stack:

    def __init__(self):

        self.top = None
        self.bottom = None
        self.length = 0

    #peek lets you see the item on top of the stack
    def peek(self):
        if self.length > 0:
            return self.top.value
        else:
            return None
     

    #adds a node to the top of the stack
    def push(self, value):

        node = Node(value)

        if(self.top is None):
            self.top = node
            self.bottom = node
            self.length += 1
        else:
            node.next = self.top            
            self.top = node
            self.length += 1

        
    #removes item from on top of the stack
    def pop(self):

        if self.length == 1:

            self.top = None
            self.bottom = None
            self.length -= 1

        elif self.length > 1:

            self.top = self.top.next
            self.length -= 1
        else:
            return None

    

myStack = Stack()
myStack.push("google")
myStack.push("udemy")
myStack.push("mozilla")
myStack.push("discord")
print(myStack.peek())
myStack.pop()
print(myStack.peek())
myStack.pop()
print(myStack.peek())
myStack.pop()
print(myStack.peek())
myStack.pop()
print(myStack.peek())

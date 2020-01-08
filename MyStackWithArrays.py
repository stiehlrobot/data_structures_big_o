class Stack:

    def __init__(self):

        self.array = []

    def peek(self):
        lastIndex = len(self.array) - 1
        print(lastIndex)
        return self.array[lastIndex]

    def push(self, value):

        self.array.append(value)

    def pop(self):

        self.array.pop(len(self.array) - 1)

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


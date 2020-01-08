class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):

        self.first = None
        self.last = None
        self.length = 0

    #get first item in line
    def peek(self):

        if self.length > 0:
            return self.first.value
        

    #adds to the queue
    def enqueue(self, value):

        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node
            self.length += 1
        elif self.length == 1:
            self.first.next = node
            self.last = node
            self.length += 1
        else:

            self.last.next = node
            self.last = node
            self.length += 1
            


    #remove the last
    def dequeue(self):
        if self.length == 1:
            self.first = None
            self.last = None
            self.length -= 1

        if self.length > 1:
            self.first = self.first.next
            self.length -= 1


que = Queue()
que.enqueue('robot')
que.enqueue('momom')
que.enqueue('smealg')
que.enqueue('barbarossa')
print(que.peek())
que.dequeue()
print(que.peek())
que.dequeue()
print(que.peek())
que.dequeue()
print(que.peek())
que.dequeue()

print(que.first)
print(que.last)
print(que.length)
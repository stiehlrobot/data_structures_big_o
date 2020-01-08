class Node:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:

    def __init__(self):

        self.root = None

    #should create a new node with the value and insert it to the right place
    def insert(self, value):
        newNode = Node(value)

        if self.root is None:
            self.root = newNode
            print("Created a root node with value {}".format(newNode.value))
            return

        compNode = self.root

        while True:           
            if newNode.value > compNode.value:
                prevVal = compNode.value
                if compNode.right is None:
                    compNode.right = newNode
                    print("added new node to right of {} with value of {}".format(prevVal , newNode.value))
                    return
                compNode = compNode.right
            elif newNode.value < compNode.value:
                prevVal = compNode.value
                if compNode.left is None:
                    compNode.left = newNode
                    print("added new node to left of {} with value of {}".format(prevVal, newNode.value))
                    return
                compNode = compNode.left
            
    
    #should return node if it is in the tree.
    #def lookup(value):

        


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
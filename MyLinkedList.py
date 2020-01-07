class ListItem:

    def __init__(self, value):

        self.value = value
        self.nextItem = None
            

class LinkedList:

    def __init__(self):

        self.head = None
        
        self.length = 0

    def append(self, itemValue):

        #create the new listitem with value of parameter itemValue
        newListItem = ListItem(itemValue)

        #if list has no items, assign the newly created listItem to the self.head variable, increment the self.length accordingly
        if self.head is None:
        
            self.head = newListItem            
            return
        
        #if list length is greater than 0 so it has at least 1 item loop to the end of the list and add the newly created list item to the end of the list
            
        current = self.head
            
        while(current.nextItem):
            current = current.nextItem               
        current.nextItem = newListItem
        return

    def append2(self, newdata):

        NewNode = ListItem(newdata)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.nextItem):
            last = last.nextItem
        last.nextItem=NewNode   
        

    def print_list(self):
        
        currentNode = self.head.value
        while currentNode is not None:            
            print(currentNode.value)
            currentNode = currentNode.nextItem
            
            
    
        


list = LinkedList()
list.append2(3)
list.print_list()
list.append2(6)
list.print_list()

list.append2(9)
list.print_list()

#list.append(16)

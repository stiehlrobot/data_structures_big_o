class myArray:

    def __init__(self):
        self.length = 0
        self.data = []


    def get_item(self, index):

        return self.data[index]

    def add_item(self, item):

        self.data[self.length-1] = item
        self.length += 1
        return self.length

    def pop_item(self):

        last_item = self.data[self.length-1]
        del last_item
        self.length -= 1
        return last_item

    def delete_item(self, index):

        item = self.data[index]
        self.shiftItems[index]

    def shift_items(self, index):
        
        for val in range(index, self.length-1):
            self.data[val] = self.data[val+1]
        del this.data[this.length-1]


arttu = myArray()
arttu.add_item('uno')
arttu.add_item('dois')
arttu.add_item('tres')
arttu.get_item(0)
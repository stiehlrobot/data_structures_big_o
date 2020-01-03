class myArray:

    def __init__(self):
        self.length = 0
        self.data = []


    def get_item(self, index):

        return self.data[index]

    def add_item(self, item):

        self.data.insert(self.length, item)         
        self.length += 1
        return self.length

    def pop_item(self):

        del self.data[-1]
        self.length -= 1
        

    def delete_item(self, index):

        item = self.data[index]
        self.shift_items(index)

    def shift_items(self, index):
        
        for val in range(index, self.length-1):
            self.data[val] = self.data[val+1]
        del self.data[-1]

    def print_items(self):

        print(self.data)



arttu = myArray()
arttu.add_item('uno')
arttu.add_item('dois')
arttu.add_item('tres')
arttu.add_item('quatro')
print(arttu.get_item(0))
print(arttu.get_item(1))
print(arttu.get_item(2))
arttu.delete_item(1)
arttu.print_items()

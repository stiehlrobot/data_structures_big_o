class HashTable:

    def __init__(self, size):

        self.data = [None for i in range(size)]

    def set(self, key, value):

        address = self._hash(key)
        if(self.data[address] == None):
            self.data[address] = []
            
        self.data[address].append([key, value])
        return self.data

    def get(self, key):

        address = self._hash(key)
        currentBucket = self.data[address]
        if(currentBucket):
            for i in range(len(currentBucket)):
                if(currentBucket[i][0] == key):
                    return currentBucket[i][1]
        return None

    def keys(self):

        keys_array = []
        for i in range(len(self.data)):
            if(self.data[i] is not None):
                print(self.data[i][1][0])
                #keys_array.append(self.data[i][0][0])
        return keys_array

    def _hash(self, key):

        hash = 0
        for i in range(2):
            hash = (hash + ord("key"[i]) * i) % len(self.data)
            print(hash)
        return hash


hashtable = HashTable(50)
hashtable.set('grapes', 10000)
hashtable.set('apples', 300)
hashtable.set('oranges', 2)
#print(hashtable.get('grapes'))
#print(hashtable.get('apples'))
print(hashtable.keys())

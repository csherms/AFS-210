class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.keys = [None] * self.size 
        self.data = [None] * self.size

    def getKeys(self):
        return self.keys
    
    def getValues(self):
        return self.data
    
    def hashfunction(self,key):
        return key % self.size
    
    def rehash(self,key):
        return key // self.size
    
    def put(self,key,data):
        # Insert your code here to store key and data 
        hashing = self.hashfunction(key)
        if self.data[hashing] == None:
            self.data[hashing] = data
            self.keys[hashing] = key
        else:
            # Update Handling
            if self.keys[hashing] == key:
                self.data[hashing] = data
            # Collision Handling
            else:
                hashing = self.rehash(key)
                if self.data[hashing] == None:
                    self.data[hashing] = data
                    self.keys[hashing] = key
                else:
                    return None
        
        
        # Must fix this get function
    def get(self,key):
        # Insert your code here to get data by key
        hashValue = self.hashfunction(key)
        if self.keys[hashValue] == key:
            return self.data[hashValue]
        else:
            hashValue = self.rehash(key)
            if self.keys[hashValue] == key:
                return self.data[hashValue]
            else:
                return None
    
    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


# Store remaining input data
H = HashTable()
H[69] = 'A'
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'

# print the slot values
print(H.getKeys())

# print the data values
print(H.getValues())

# print the value for key 52
print(H[52])
print(H[80])
print(H[70])
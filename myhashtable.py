# Hashtable with open addressing and linear probe

class myhashtable:
    
    def __init__(self, initial_size=10, load_factor=0.8):
        self.size = initial_size
        self.tot = 0
        self.table = [None] * self.size
        self.load_factor = load_factor
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def table_size(self):
        return self.size
    
    def num_size(self):
        return self.tot

    def change_size(self, multi_factor=2):
        self.size *= multi_factor
        temp_table = [None] * self.size
        for key_value in self.table:
            if (key_value):
                key, value = key_value
                hashcode = self.hash_function(key)
                while (temp_table[hashcode]):
                    hashcode = (hashcode + 1) % self.size
                temp_table[hashcode] = (key, value)
        self.table = temp_table

    def add(self, key, value):
        hashcode = self.hash_function(key)
        if (self.tot / self.size > self.load_factor):
            self.change_size()
        while (self.table[hashcode]):
            hashcode = (hashcode + 1) % self.size
        self.table[hashcode] = (key, value)
        self.tot += 1


    def search(self, key):
        hashcode = self.hash_function(key)
        while (self.table[hashcode] and self.table[hashcode][0] != key):
            hashcode = (hashcode + 1) % self.size
        if (not self.table[hashcode]):
            return "not found"
        return self.table[hashcode][1]

    def clear(self):
        self.__init__()

    def print_whole_hashtable(self):
        for key_value in self.table:
            if (key_value):
                key, value = key_value
                print(key, value)
    

        



    

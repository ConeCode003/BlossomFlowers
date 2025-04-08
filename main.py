from linked_list import Node, LinkedList
from blossom_lib import flower_def


class HashMap:
    def __init__(self, size=0):
        self.size = size
        self.array = [LinkedList() for i in range(size)]  # every head is None type

    def hash(self, key):
        hash_code = sum(key.encode())
        return hash_code

    def compress(self, hash_code):
        return hash_code % self.size

    def assign(self, key, value):
        hash_code = self.hash(key)
        array_index = self.compress(hash_code)
        payload = Node([key, value])
        list_at_array = self.array[array_index]  # dobijamo listu u nizu
        for item in list_at_array:
            if item[0] == key:
                item[1] = value
                return
        list_at_array.insert(payload)

    def retrieve(self, key):
        hash_code = self.hash(key)
        array_index = self.compress(hash_code)
        list_at_index = self.array[array_index]  # lista na indeksu
        # odavde dobijes linked listu
        for item in list_at_index:
            if item is not None and item[0] == key:
                return item[1]
        return None


blossom = HashMap(len(flower_def))
for flower in flower_def:
    blossom.assign(flower[0], flower[1])
print(blossom.retrieve('daisy'))

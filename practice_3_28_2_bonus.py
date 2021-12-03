class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

    def __repr__(self):
        return f"{self.key} => {self.val}"


class HashTable:

    def __init__(self, size):
        self.size = size
        self.items = [None]*self.size

    def put(self, key, val):
        new_data = Node(key, val)
        ind = self.hash_it(key)
        if not self.items[ind]:
            self.items[ind] = new_data

        elif self.items[ind]:
            current = self.items[ind]
            while current:
                if current.key == key:
                    current.val = val
                if not current.next:
                    current.next = new_data
                    break
                current = current.next

    def get(self, key):
        ind = self.hash_it(key)
        current = self.items[ind]
        while current:
            if current.key == key:
                return current
            current = current.next
        raise IndexError(f"No data with such key: {key}")

    def hash_it(self, key):
        if isinstance(key, int):
            return key % self.size

        elif isinstance(key, str):
            return sum([ord(x) for x in key]) % self.size

        raise TypeError(f"Wrong  {key} of type {type(key)}")


hash_table = HashTable(7)

hash_table.put(21, "cdd")
hash_table.put(13, "back")
hash_table.put(14, "Arc")
hash_table.put("bass", 11)
hash_table.put("pac", 37)
hash_table.put(76, 3)
hash_table.put(4, "o")

print(hash_table.get(11))

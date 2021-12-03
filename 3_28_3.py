class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __repr__(self):
        return f"{self.key} => {self.val}"


class HashTable:

    def __init__(self, size):
        self.size = size
        self.items = [None]*self.size

    def put(self, key, val):
        new_data = Node(key, val)
        ind = self.hash_it(key)
        start_ind = ind
        while self.items[ind]:
            if self.items[ind].key == key:          # Обновление елемента по ключу
                self.items[ind].val = val
                return
            ind = self.rehash_it(ind)
            if ind == start_ind:
                raise IndexError("The Hash table is fully")

        self.items[ind] = new_data

    def hash_it(self, key):
        if isinstance(key, int):
            return key % self.size

        elif isinstance(key, str):
            return sum([ord(x) for x in key]) % self.size

        raise TypeError(f"Wrong  {key} of type {type(key)}")

    def rehash_it(self, key):
        return (key + 1) % self.size

    def get(self, key):
        ind = self.hash_it(key)
        start_ind = ind
        while True:
            if self.items[ind] and self.items[ind].key == key:
                return self.items[ind].val
            else:
                ind = self.rehash_it(ind)
            if ind == start_ind:
                raise IndexError(f"No data with such key: {key}")

    def delete(self, key):
        ind = self.hash_it(key)
        start_ind = ind
        while True:
            if self.items[ind] and self.items[ind].key == key:
                self.items[ind] = None
                return
            else:
                ind = self.rehash_it(ind)
            if ind == start_ind:
                break

    def __len__(self):
        i = 0
        for node in self.items:
            if node:
                i += 1
        return i

    def __contains__(self, key):
        ind = self.hash_it(key)
        start_ind = ind
        while True:
            if self.items[ind] and self.items[ind].key == key:
                return True
            else:
                ind = self.rehash_it(ind)
            if ind == start_ind:
                break

        return False


hash_table = HashTable(7)
print(hash_table.items)

hash_table.put(21, "cdd")
hash_table.put(13, "back")
hash_table.put(11, "Arc")
hash_table.put("bass", 11)
hash_table.put("pac", 37)
hash_table.put(76, 3)
hash_table.put(4, "o")

print(hash_table.items)

hash_table.delete(21)

print(hash_table.items)

print(76 in hash_table)
print(len(hash_table))

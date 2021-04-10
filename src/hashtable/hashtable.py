class HashTable:
    def __init__(self, size: int):
        if size < 1:
            raise IndexError('Size of hashtable should be minimum 1')
        self.size = size
        self.data = [None] * size

    def _hash(self, key):
        hash_data = 0
        for i in range(len(key)):
            hash_data = (hash_data + ord(key[i]) * i) % self.size
        return hash_data

    def __setitem__(self, key, value):
        if not (None in self.data):  # Checking self.data != None
            raise IndexError('Exceeding hashtable limit')
        pointer = self._hash(key)
        if not self.data[pointer]:
            self.data[pointer] = []
        else:
            i = 0
            for k, v in self.data[pointer]:
                if k == key:
                    self.data[pointer][i][1] = value
                    return True
                i += 1
        self.data[pointer].append([key, value])
        return True

    def __getitem__(self, key):
        pointer = self._hash(key)
        items = self.data[pointer]
        if items:
            for k, v in items:
                if k == key:
                    return v
        return False

    def __repr__(self):
        my_set = set()
        for items in self.data:
            if items:
                for single_item in items:
                    data_element = "{key}: {value}".format(key=single_item[0], value=single_item[1])
                    my_set.add(data_element)
        return str(my_set)

    def items(self) -> list:
        """
        Returns list of tuples contains [(key, value), ...]
        :return: list
        """
        hashtable_items = []
        for items in self.data:
            if items:  # Checking self.data != None
                for item_data in items:
                    hashtable_items.append(tuple(item_data))
        return hashtable_items

    def keys(self) -> list:
        """
        Returns list of keys
        :return: list
        """
        hashtable_keys = []
        for items in self.data:
            if items:  # Checking self.data != None
                for item_data in items:
                    hashtable_keys.append(item_data[0])
        return hashtable_keys

    def values(self) -> list:
        """
        Returns list of values
        :return: list
        """
        hashtable_keys = []
        for items in self.data:
            if items:  # Checking self.data != None
                for item_data in items:
                    hashtable_keys.append(item_data[1])
        return hashtable_keys

    def delete(self, key) -> bool:
        """
        Delete an element using key
        :param key: key
        :return: bool
        """
        for items in self.data:
            if items:
                for item_data in items:
                    if item_data[0] == key:
                        index = self.data.index(items)
                        self.data[index].remove(item_data)
                        return True
        return False

if __name__ == '__main__':
    my_hashtable = HashTable(5)
    my_hashtable['graphs'] = False
    my_hashtable['mango'] = 'google'
    my_hashtable['mango2'] = 100
    my_hashtable.delete('mango2')
    print(my_hashtable.items())
    print(my_hashtable.keys())
    print(my_hashtable.values())
    data = my_hashtable['mango']
    print(data)
    print(my_hashtable)

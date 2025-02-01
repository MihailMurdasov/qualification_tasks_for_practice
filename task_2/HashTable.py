class HashTable:
    def __init__(self, capacity=8, load_factor=0.7):
        self.capacity = capacity
        self.size = 0
        self.load_factor = load_factor
        self.keys = [None] * capacity
        self.values = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def _quadratic_probe(self, index, i):
        return (index + i ** 2) % self.capacity

    def put(self, key, value):
        self.__setitem__(key, value)

    def get(self, key):
        return self.__getitem__(key)

    def remove(self, key):
        self.__delitem__(key)

    def __setitem__(self, key, value):
        if self.size / self.capacity >= self.load_factor:
            self._rehash()

        index = self._hash(key)
        i = 0
        while self.keys[index] is not None and self.keys[index] != key:
            i += 1
            index = self._quadratic_probe(index, i)

        if self.keys[index] is None:
            self.size += 1

        self.keys[index] = key
        self.values[index] = value

    def __getitem__(self, key):
        index = self._hash(key)
        i = 0
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            i += 1
            index = self._quadratic_probe(index, i)
        raise KeyError(f"Key '{key}' not found")

    def __delitem__(self, key):
        index = self._hash(key)
        i = 0
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.size -= 1
                return
            i += 1
            index = self._quadratic_probe(index, i)
        raise KeyError(f"Key '{key}' not found")

    def __contains__(self, key):
        index = self._hash(key)
        i = 0
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return True
            i += 1
            index = self._quadratic_probe(index, i)
        return False

    def __len__(self):
        return self.size

    def _rehash(self):
        old_keys = self.keys
        old_values = self.values
        self.capacity *= 2
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

        for key, value in zip(old_keys, old_values):
            if key is not None:
                self[key] = value

    def get_keys(self):
        return [key for key in self.keys if key is not None]

    def get_values(self):
        return [self.values[i] for i in range(self.capacity) if self.keys[i] is not None]

    def get_items(self):
        return [(self.keys[i], self.values[i]) for i in range(self.capacity) if self.keys[i] is not None]
class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return int(key) % self.size  # Usando o número da conta como chave

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            # Evitar colisão inserindo uma nova entrada na lista ligada do bucket
            self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return None
        for account in self.table[index]:
            if account[0] == key:
                return account[1]
        return None

    def update(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            return False
        for i, account in enumerate(self.table[index]):
            if account[0] == key:
                self.table[index][i] = (key, value)
                return True
        return False
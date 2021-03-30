class MyHashSet:
    def __init__(self):
        self.list = set

    def add(self, key: int):
            self.list.add(key)

    def remove(self, key: int):
        if key in self.l:
            self.list.remove(key)

    def contains(self, key: int):
        return key in self.list
class RandomizedSet:
    def __init__(self):
        self.value_to_index = {}
        self.values = []

    def insert(self, val):
        if val in self.value_to_index:
            return False
        self.value_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        if val not in self.value_to_index:
            return False
        index_to_remove = self.value_to_index[val]
        last_value = self.values[-1]
        self.values[index_to_remove] = last_value
        self.value_to_index[last_value] = index_to_remove
        self.values.pop()
        del self.value_to_index[val]
        return True

    def getRandom(self):
        return random.choice(self.values)
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = list()

    def push(self, item):
        if item not in self.storage:
            self.storage.append(item)
            self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()
        return None

    def len(self):
        return self.size

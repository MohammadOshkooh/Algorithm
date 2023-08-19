class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = value
        elif value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def search(self, value):
        if self.value == value:
            return self
        elif value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.search(value)
        else:
            if self.right is None:
                return None
            else:
                return self.right.search(value)

    def find_index(self, value, index=0):
        if self.value == value:
            return index
        elif value < self.value:
            if self.left is None:
                return -1
            else:
                return self.left.find_index(value, index=index * 2 + 1)
        else:
            if self.right is None:
                return -1
            else:
                return self.right.find_index(value, index=index * 2 + 2)


array = [1, 2, 6, 5, 2, 16, 4, 55, 17, 21, 0, 12, 11, 10]

root = Node()

for num in array:
    root.insert(num)

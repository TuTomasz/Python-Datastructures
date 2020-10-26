class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CircularLinkedList:
    # Declaring head and tail pointer as null.
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def add(self, data):
        pass

    def remove(self):
        pass

    def getNext(self):
        pass

    def getPrevious(self):
        pass

    def getSize(self):
        pass

    def isEmpty(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

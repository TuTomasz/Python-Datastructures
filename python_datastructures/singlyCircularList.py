class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.sentinel = False


class singlyCircularList:
    # Declaring head and tail pointer as null.
    def __init__(self):
        self.__sentinel = Node(None)
        self.__sentinel.sentinel = True
        self.__head = self.__sentinel
        self.__tail = self.__sentinel
        self.__current = self.__head
        self.__size = 0
        

    def add(self, value):
        """Add element to circular list.

        Args:
            value (Any): value to be added.
        """
        newNode = Node(value)
        if self.__size == 0:
            self.__sentinel.next = newNode
            newNode.next = self.__sentinel
            self.__head = newNode
            self.__tail = newNode
            self.__size += 1
        else:
            self.__tail.next = newNode
            newNode.next = self.__sentinel
            self.__tail = newNode
            self.__size += 1

    def remove(self):
        pass

    def getNext(self):

        if self.__size == 0:
            return None
        else:
            valueToReturn = self.__current.value
            if self.__current.next.sentinel == True:
                self.__current = self.__head
            else:
                self.__current = self.__current.next
            return valueToReturn

    def getHead(self):
        """Get referance to head node in circular list.

        Returns:
            Node: referance of head node.
        """
        return self.__head

    def getTail(self):
        """Get referance to tail node in circular list.

        Returns:
            Node: referance of tail node.
        """
        return self.__tail

    def getHeadValue(self):
        """Get value of head in circular list.

        Returns:
            Element: value of head node.
        """
        return self.__head.value

    def getTailValue(self):
        """Get value of tail in circular list.

        Returns:
            Element: value of tail node.
        """
        return self.__tail.value

    def getSize(self):
        """Get size of the circular list.

        Returns:
            integer: number of elements in the queue.
        """
        return self.__size

    def isEmpty(self):
        """Check if circular list is empty.

        Returns:
            boolean: True if no elements in the stack.
        """
        return True if self.__size == 0 else False

    def __str__(self):
        """Get string representation of the circular list.

        Returns:
            String: prints string representation of the stack.
        """
        arr = []
        current = self.__head
        while current:
            if current.sentinel == True:
                break
            arr.append(current.value)
            current = current.next
        return str(arr)

    def __len__(self):
        return self.__size


if __name__ == "__main__":
    l = singlyCircularList()
    print(l.getHead())
    l.add(3)
    print(l.getHead().value, l.getTail().value)
    l.add(5)
    print(l.getHead(), l.getTail())
    print(l)
    print(len(l),'j')

    print(l.getNext())
    print(l.getNext())
    print(l.getNext())
    print(l.getNext())
    print(l.getNext())
    print(l.getNext())
   

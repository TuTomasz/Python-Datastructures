
class MinHeap:

    def __init__(self, array):
        """Initialize a min Heap

        Args:
            array (number): Array to turn into a a heap
        """
        self.heap = self.build(array)

    def build(self, array):
        """Build a min Heap

        Args:
            array (numbers): Array to turn into a a heap
        Returns:
            array: Heap representation of the array
        """
        firstParrentIdx = (len(array) - 1 // 2)
        for currentIdx in reversed(range(firstParrentIdx)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        """Sift element down to restore heap order

        Args:
            currentIdx (integer): index of current position
            endIdx (integer): index of the last element
            heap (array): array representation of heap
        """
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1

            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(idxToSwap, currentIdx, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                break

    def siftUp(self, currentIdx, heap):
        """Sift element up to restore heap order

        Args:
            currentIdx (integer): index of current position
            heap (array): array representation of heap
        """

        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(parentIdx, currentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        """Look up the smallest element

        Returns:
            Number: heap smallest element
        """
        return self.heap[0]

    def add(self, val):
        """Add element to the heap

        Args:
            val (number): Element to be added to the heap
        """

        self.heap.append(val)
        self.siftUp(len(self.heap) - 1, self.heap)

    def remove(self):
        """Remove Smallest element from the heap

        Returns:
            number: smallest element in the heap
        """

        self.swap(0, len(self.heap) - 1, self.heap)
        removed = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return removed

    def swap(self, i, j, heap):
        """Helper method for swapping elements in the heap

        Args:
            i (index): element one index
            j (index): element two index
            heap (array): array representation of the heap
        """

        heap[j], heap[i] = heap[i], heap[j]

    def __str__(self):

        return str(self.heap)

    def __len__(self):
        return len(self.heap)


class MaxHeap:
    def __init__(self, array):
        """Initialize a max Heap

        Args:
            array (number): Array to turn into a a heap
        """
        self.heap = self.build(array)

    def build(self, array):
        """Build a min Heap

        Args:
            array (numbers): Array to turn into a a heap

        Returns:
            array: Heap representation of the array
        """
        firstParrentIdx = (len(array) - 1 // 2)
        for currentIdx in reversed(range(firstParrentIdx)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        """Sift element down to restore heap order

        Args:
            currentIdx (integer): index of current position
            endIdx (integer): index of the last element
            heap (array): array representation of heap
        """
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1

            if childTwoIdx != -1 and heap[childTwoIdx] > heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            if heap[idxToSwap] > heap[currentIdx]:
                self.swap(idxToSwap, currentIdx, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                break

    def siftUp(self, currentIdx, heap):
        """Sift element up to restore heap order

        Args:
            currentIdx (integer): index of current position
            heap (array): array representation of heap
        """
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] > heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        """Look up the smallest element

        Returns:
            Number: heap smallest element
        """
        return self.heap[0]

    def add(self, value):
        """Add element to the heap

        Args:
            val (number): Element to be added to the heap
        """

        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def remove(self):
        """Remove smallest element from the heap

        Returns:
            number: smallest element in the heap
        """

        self.swap(0, len(self.heap) - 1, self.heap)
        removed = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return removed

    def swap(self, i, j, heap):
        """Helper method for swapping elements in the heap

        Args:
            i (index): element one index
            j (index): element two index
            heap (array): array representation of the heap
        """

        heap[i], heap[j] = heap[j], heap[i]

    def __str__(self):

        return str(self.heap)

    def __len__(self):
        return len(self.heap)


if __name__ == "__main__":
    pass

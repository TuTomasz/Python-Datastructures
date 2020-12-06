"""Heap is a specialized tree-based data structure which is essentially an almost complete[1] tree that satisfies the heap property: in a max heap, for any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C. In a min heap, the key of P is less than or equal to the key of C.[2] The node at the "top" of the heap (with no parents) is called the root node."""

from typing import TypeVar


T = TypeVar("T")


class MinHeap:
    def __init__(self, array: list):

        """Initialize a min Heap"""

        self.heap = self.build(array)

    def build(self, array: list) -> list:

        """Build a min Heap"""

        firstParrentIdx = len(array) - 1 // 2
        for currentIdx in reversed(range(firstParrentIdx)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx: int, endIdx: int, heap: list) -> None:

        """Sift element down to restore heap order"""

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

    def siftUp(self, currentIdx: int, heap: list) -> None:

        """Sift element up to restore heap order"""

        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(parentIdx, currentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self) -> T:

        """Look up the smallest element"""

        return self.heap[0]

    def add(self, val: T) -> None:

        """Add element to the heap"""

        self.heap.append(val)
        self.siftUp(len(self.heap) - 1, self.heap)

    def remove(self) -> T:

        """Remove Smallest element from the heap"""

        self.swap(0, len(self.heap) - 1, self.heap)
        removed = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return removed

    def swap(self, i: int, j: int, heap: list) -> None:

        """Helper method for swapping elements in the heap"""

        heap[j], heap[i] = heap[i], heap[j]

    def __str__(self) -> str:

        return str(self.heap)

    def __len__(self) -> int:
        return len(self.heap)


class MaxHeap:
    def __init__(self, array: list):

        """Initialize a max Heap"""

        self.heap = self.build(array)

    def build(self, array: list) -> list:

        """Build a min Heap"""

        firstParrentIdx = len(array) - 1 // 2
        for currentIdx in reversed(range(firstParrentIdx)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx: int, endIdx: int, heap: list) -> None:

        """Sift element down to restore heap order"""

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

    def siftUp(self, currentIdx: int, heap: list) -> None:

        """Sift element up to restore heap order"""

        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] > heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self) -> T:

        """Look up the smallest element"""

        return self.heap[0]

    def add(self, value: T) -> None:

        """Add element to the heap"""

        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def remove(self) -> T:

        """Remove smallest element from the heap"""

        self.swap(0, len(self.heap) - 1, self.heap)
        removed = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return removed

    def swap(self, i: int, j: int, heap: list) -> None:

        """Helper method for swapping elements in the heap"""

        heap[i], heap[j] = heap[j], heap[i]

    def __str__(self) -> str:

        return str(self.heap)

    def __len__(self) -> int:
        return len(self.heap)


if __name__ == "__main__":
    pass

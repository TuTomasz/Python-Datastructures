

# Python-Datastructures

Python-Datastructures is a Python library containing  implementations of various data structures in Python that can be used in your projects. Useful when preparing for interviews or buiding school projects. Focus on developing your algorithms and not worry about finding python implementations of classic data structures.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install python-datastructures.

```bash
pip install python-datastructures
```

## Usage
Sample usage of the library. Import any datastructure from the list of supported datastructures.

* Stack
* Queue
* SinglyLinkedList
* DoublyLinkedList
* MaxHeap
* MinHeap
* Trie

```python
from python_datastructures import Stack

stack = Stack()
stack.push(3)
stack.push(4)

print(stack) # returns [3,4]
```
## Datastructure Methods

<div align="center"> <h2>Stack</h2></div>

|  Methood  | Description                               | Args  | Return  |
|:---------:|-------------------------------------------|-------|---------|
| push()    | Add element to the top of the stack.      | value | None    |
| pop()     | Remove element from the top of the stack. | None  | Node   |
| peek()    | View top element in the stack.            | None  | value   |
| isEmpty() | Check if stack is empty.                  | None  | Boolean |
| getSize() | Get number of elements in the stack.      | None  | Integer |
| \__str__() | Return string representation of stack    | None  | String  |

<br></br>
<div align="center"> <h2>Queue</h2></div>

|  Methood  | Description                           | Args  | Return  |
|:---------:|---------------------------------------|-------|---------|
| getHead() | View first element in the queue.      | None  | Value   |
| getTail() | View last element in the queue.       | None  | Value   |
| enqueue() | Add element to the queue.             | Value | None    |
| dequeue() | Remove element from queue.            | None  | Node   |
| isEmpty() | Check if queue is empty.              | None  | Boolean |
| getSize() | Get number of elements in the queue.  | None  | Integer |
| \__str__() | Return string representation of queue | None  | String  |

<br></br>
<div align="center"> <h2>Trie</h2></div>

|   Methood  | Description                                            | Args   | Return  |
|:----------:|--------------------------------------------------------|--------|---------|
| build()    | Builds a trie structure given array of words           | Array  | None    |
| add()      | Add word to the trie structure.                        | String | None    |
| contains() | Checks if a trie contains a word or substring of word. | String | Boolean |

<br></br>
<div align="center"> <h2>Min/Max Heap</h2></div>

|  Methood | Description                           | Args  | Return |
|:--------:|---------------------------------------|-------|--------|
| build()  | Build a Heap from Array of Elements   | Array | Array  |
| peek()   | Look up top element in Heap           | None  | Value  |
| add()    | Add element to the Heap.              | Value | None   |
| remove() | Remove Smallest element from the Heap | None  | Value  |






<br></br>
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
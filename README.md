# Linked List Implementation in Python

This repository contains a simple implementation of a singly linked list in Python. The linked list supports operations like appending nodes, deleting nodes, and printing the list. It also includes the ability to insert nodes at the beginning or after a specified node.

## Features
- **Append nodes**: Adds a new node to the end of the list or after a specific node.
- **Insert at the beginning**: Allows inserting a node at the start of the list.
- **Delete nodes**: Removes a node by its value.
- **Print list**: Prints the current list of nodes in a readable format.

## Classes
### `Node`
The `Node` class represents a single node in the linked list. It contains:
- `val`: The value of the node.
- `next`: A reference to the next node in the list (initially `None`).

#### Methods:
- `__init__(val)`: Initializes a new node with the given value `val`.

### `LinkedList`
The `LinkedList` class represents the linked list itself and contains the following methods:

#### Methods:
- `__init__()`: Initializes the linked list with an empty list (head is `None`).
- `append(data, data1=None)`: Adds a new node with the value `data`:
  - If `data1` is provided, the node is inserted after the node with value `data1`.
  - If `data1` is `"beginning"`, the new node is added at the beginning.
  - If `data1` is `None`, the new node is appended to the end of the list.
- `delete(data)`: Deletes the node with the value `data`.
  - If the node is the head, it removes the head.
  - If the node is the last node, it updates the previous node's `next` pointer.
  - If the node is found in the middle, it adjusts the pointers accordingly.
- `printlist()`: Prints all the values in the list in a readable format (`val -> val -> ... -> End`).

## Usage

### Example Code

```python
if __name__ == "__main__":
    l = LinkedList()

    # Append nodes
    l.append(5)          # Add 5 at the end
    l.printlist()         # Output: 5 -> End

    l.append(10, 5)      # Add 10 after 5
    l.printlist()         # Output: 5 -> 10 -> End

    l.append(12, 5)      # Add 12 after 5
    l.printlist()         # Output: 5 -> 12 -> 10 -> End

    # Delete nodes
    l.delete(12)         # Remove node with value 12
    l.printlist()         # Output: 5 -> 10 -> End

    l.delete(5)          # Remove node with value 5 (head)
    l.printlist()         # Output: 10 -> End

    # Insert at the beginning
    l.append(5, "beginning")
    l.printlist()         # Output: 5 -> 10 -> End

    # Insert after a node
    l.append(12, 5)
    l.printlist()         # Output: 5 -> 12 -> 10 -> End

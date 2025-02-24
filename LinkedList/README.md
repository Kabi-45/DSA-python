# Linked Lists

A linked list is a non-contiguous data structure composed of nodes, where each node contains:
- Data value
- Reference (pointer) to the next node

### Key Characteristics
- Non-contiguous memory allocation
- Sequential access from head node
- Dynamic size allocation
- Efficient insertions/deletions at known positions

### Implementation Example
```python
class Node:
    def __init__(self, data):
        self.data = data  # Store value
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initially empty

    def append(self, data):
        """Add a new node at the end of the linked list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        """Print the linked list"""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def insert_at_beginning(self, data):
        """ Insert new node at the beginning of the linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        """Delete the node"""
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        while temp:
            if temp.next and temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next
# Usage Example
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_list()  # Output: 10 -> 20 -> 30 -> None
```

## Arrays vs Linked Lists in Python:

## Arrays

An array is a contiguous block of memory where elements are stored sequentially, allowing O(1) time access via indexing.

### Key Characteristics
- Contiguous memory storage
- Direct index-based access (O(1))
- Fixed size in some languages (dynamic in Python)
- O(n) complexity for insertions/deletions in middle/beginning


## Comparison Table

| Feature | Array | Linked List |
|---------|-------|-------------|
| Memory Storage | Contiguous | Non-contiguous |
| Access Time | O(1) | O(n) |
| Insertion/Deletion | O(n) mid/beginning | O(1) at head |
| Size | Fixed (language dependent) | Dynamic |
| Memory Usage | Efficient | Additional overhead |

## Time Complexity

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Access    | O(1)  | O(n)        |
| Search    | O(n)  | O(n)        |
| Insertion (beginning) | O(n) | O(1) |
| Insertion (end) | O(1)* | O(n) |
| Deletion (beginning) | O(n) | O(1) |
| Deletion (end) | O(1) | O(n) |
| Space Complexity | O(n) | O(n) |

*Amortized time complexity for dynamic arrays

## When to Use Each

### Choose Arrays When:
- Random access is frequent
- Size is known and fixed
- Memory efficiency is crucial

### Choose Linked Lists When:
- Frequent insertions/deletions
- Dynamic size requirements
- Memory fragmentation is acceptable


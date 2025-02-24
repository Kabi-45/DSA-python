# Class representing a single node in the linked list
class Node:
    def __init__(self, data):
        """
        Constructor to initialize a node with data.
        Each node has:
        - `data`: The value stored in the node.
        - `next`: Pointer to the next node (default is None).
        """
        self.data = data
        self.next = None  # Initially, the node does not point to any other node

# Class representing the linked list
class LinkedList:
    def __init__(self):
        """
        Constructor to initialize an empty linked list.
        - `head`: Points to the first node in the list (initially None).
        """
        self.head = None

    def nothead(self, node):
        """
        Ensures that the first inserted node becomes the head of the list.
        If `head` is None (empty list), assigns the new node as `head`.
        """
        if not self.head:
            self.head = node  # Assign new node as head
            return True  # Indicating that head was assigned
        return False  # Head was already assigned, do nothing

    def traverse(self, node):
        """
        Traverses the list to find the last node.
        Returns the last node in the list.
        """
        temp = node  # Start from the given node
        while temp.next:  # Move until `next` is None (end of the list)
            temp = temp.next
        return temp  # Return the last node found

    def append(self, data):
        """
        Adds a new node with the given data at the end of the linked list.
        Steps:
        1. Create a new node.
        2. If list is empty, set the new node as the head.
        3. Otherwise, find the last node and link it to the new node.
        """
        new_node = Node(data)  # Step 1: Create a new node

        if not self.head:
            self.head = new_node  # Assign new node as head
            # Step 2: If list is empty, new_node becomes head
            return  # Exit the function since head is already set

        last_node = self.traverse(self.head)  # Step 3: Find last node
        last_node.next = new_node  # Link last node to new node

    def insert_at_beginning(self, data):
        """
        Inserts a new node with given data at the beginning of the linked list.
        Steps:
        1. Create a new node.
        2. Make the new node point to the current head.
        3. Update head to the new node.
        """
        new_node = Node(data)  # Step 1: Create a new node
        new_node.next = self.head  # Step 2: Link new node to the current head
        self.head = new_node  # Step 3: Update head to the new node


    def delete_at_beginning(self):
        """
        Deletes the first node (head) of the linked list.
        Steps:
        1. Check if the list is empty (nothing to delete).
        2. Move the head pointer to the second node.
        """
        if self.head is None:  # Step 1: Check if the list is empty
            print("List is empty! Nothing to delete.")
            return

        self.head = self.head.next  # Step 2: Move head to next node

    def delete(self, key):
        """
        Deletes the first node that contains the given key.
        
        Steps:
        1. If the head node contains the key, update the head.
        2. Otherwise, search for the key in the list.
        3. Adjust links to remove the node safely.
        """
        
        temp = self.head  # Start from the head of the list

        # Case 1: If the head itself holds the key, update the head
        if temp is not None and temp.data == key:
            self.head = temp.next  # Move head to the next node
            temp = None  # Free the memory (optional in Python, as garbage collector handles it)
            return

        # Case 2: Search for the node with the given key
        prev = None  # Keep track of the previous node
        while temp is not None and temp.data != key:
            prev = temp  # Store the previous node
            temp = temp.next  # Move to the next node

        # Case 3: If key was not found in the linked list
        # where prev is the last 
        if temp is None:
            print("Key not found in the list!")
            return

        # Case 4: Node with the key found, unlink it from the linked list
        prev.next = temp.next  # Bypass the node to be deleted
        temp = None  # Free the memory (again, optional in Python)


    def print_list(self):
        """
        Prints the linked list in a readable format.
        Steps:
        1. Start from head.
        2. Traverse each node and print its data.
        """
        temp = self.head  # Start from head
        while temp:  # Iterate through the list until reaching None
            print(temp.data, end=" -> ")  # Print node's data
            temp = temp.next  # Move to next node
        print("None")  # Indicate end of the list

# Driver code to test the LinkedList
if __name__ == "__main__":
    ll = LinkedList()  # Create an empty linked list

    ll.append(10)  # Add 10
    ll.append(20)  # Add 20
    ll.append(30)  # Add 30
    ll.insert_at_beginning(5)  # Insert 5 at the beginning

    ll.print_list()  # Expected Output: 5 -> 10 -> 20 -> 30 -> None

class Node:
    def __init__(self, value, next=None):
        # Initialize the node with a value and a reference to the next node (which is None by default)
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        # Initialize an empty linked list
        self.head = None
        self.tail = None

    def append(self, value):
        # Add a new node with the given value to the end of the list
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        # Add a new node with the given value to the beginning of the list
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, value):
        # Remove the first node with the given value from the list
        current_node = self.head
        if current_node.value == value:
            self.head = current_node.next
            if self.head is None:
                self.tail = None
            return
        while current_node.next is not None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                if current_node.next is None:
                    self.tail = current_node
                return
            current_node = current_node.next

    def contains(self, value):
        # Return a boolean indicating whether the given value is in the list
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def print_list(self):
        # Print the values of all the nodes in the list
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

# Create a new linked list
linked_list = LinkedList()

# Add some nodes to the list
values = input("Enter a list of values to add to the linked list: ").split()
for value in values:
    linked_list.append(value)

# Print the list
print("Linked list:")
linked_list.print_list()

# Check if the list contains a given value
value_to_find = input("Enter a value to search for in the linked list: ")
if linked_list.contains(value_to_find):
    print(f"The linked list contains {value_to_find}.")
else:
    print(f"The linked list does not contain {value_to_find}.")
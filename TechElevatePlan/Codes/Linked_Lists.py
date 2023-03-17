class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

# Create the nodes and link them together
node_1 = Node("once")
node_2 = Node("upon")
node_3 = Node("a")
node_4 = Node("time")
node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def read(self, index):
        # Begin at the first node of the list:
        current_node = self.first_node
        current_index = 0

        # Keep following the links of each node until we get to the index we're looking for
        while current_index < index:
            # If we're past the end of the list, return None
            if not current_node:
                return None
            current_node = current_node.next_node
            current_index += 1

        # Return the data of the current node
        return current_node.data

    def index_of(self, value):
        # Begin at the first node of the list:
        current_node = self.first_node
        current_index = 0

        # Search through the list until we find the value we're looking for
        while current_node:
            # If we find the data we're looking for, return its index
            if current_node.data == value:
                return current_index
            current_node = current_node.next_node
            current_index += 1

        # If we get through the entire list without finding the data, return None
        return None

    def insert_at_index(self, index, value):
        # Create the new node with the provided value:
        new_node = Node(value)

        # If we are inserting at the beginning of the list:
        if index == 0:
            # Have our new node link to what was the first node:
            new_node.next_node = self.first_node
            # Establish that our new node is now the list's first node:
            self.first_node = new_node
            return

        # If we are inserting anywhere other than the beginning:
        current_node = self.first_node
        current_index = 0

        # First, we access the node immediately before where the new node will go:
        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1

        # Have the new node link to the next node:
        new_node.next_node = current_node.next_node
        # Modify the link of the previous node to point to our new node:
        current_node.next_node = new_node

    def delete_at_index(self, index):
        # If we are deleting the first node:
        if index == 0:
            # Simply set the first node to be what is currently the second node:
            self.first_node = self.first_node.next_node
            return

        current_node = self.first_node
        current_index = 0

        # First, we find the node immediately before the one we want to delete and call it current_node:
        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1

        # We find the node that comes after the one we're deleting:
        node_after_deleted_node = current_node.next_node.next_node

        # We change the link of the current_node to point to the node_after_deleted_node, leaving the node we want
        # to

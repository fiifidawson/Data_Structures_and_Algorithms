""" Implementing Linked Lists"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self, first_node=None):
        self.first_node = first_node

    def read(self, index):
        # We begin at the first node of the list:
        current_node = self.first_node
        current_index = 0
        while current_index < index:
            # We keep following the links of each node until we get to the
            # index we're looking for:
            current_node = current_node.next_node
            current_index += 1
            # If we're past the end of the list, that means the
            # value cannot be found in the list, so return None:
            if not current_node:
                return None
        return current_node.data

    def index_of(self, value):
        # We begin at the first node of the list:
        current_node = self.first_node
        current_index = 0
        while current_node:
            # If we find the data we're looking for, we return its index:
            if current_node.data == value:
                return current_index
            # Otherwise, we move on to the next node:
            current_node = current_node.next_node
            current_index += 1
        # If we get through the entire list without finding the data, we return None:
        return None

    def insert_at_index(self, index, value):
        # We create the new node with the provided value:
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
        # We change the link of the current_node to point to the node_after_deleted_node, leaving the node we want to delete out of the list:
        current_node.next_node = node_after_deleted_node

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self, first_node=None):
        self.first_node = first_node

    def read(self, index):
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            current_node = current_index.next
            current_index += 1

            if not current_node:
                return None
        return current_node.data
    
    def index_of(self, value):
        current_node = self.first_node
        current_index = 0

        while current_node:
            if current_node == value:
                return current_index
        
            current_node = current_node.next
            current_index += 1
        return None 

    def insert_at_index(self, index, value):
        new_node = Node(value)

        if index == 0:
            pass   
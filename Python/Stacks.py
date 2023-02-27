class Stack:
    def __init__(self):
        # Initialize an empty list to hold the elements of the stack
        self.data = []

    def push(self, element):
        # Append the given element to the end of the list
        self.data.append(element)

    def pop(self):
        # Remove and return the last element of the list
        return self.data.pop()

    def read(self):
        # Return the last element of the list without removing it
        # Return None if the list is empty
        return self.data[-1] if len(self.data) > 0 else None

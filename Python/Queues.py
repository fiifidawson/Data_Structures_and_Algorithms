class Queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, element):
        self.data.append(element)
    
    def dequeue(self):
        # The Python pop method with index 0 removes and returns the
        # first element of a list:
        return self.data.pop(0)
    
    def read(self):
        return self.data[0]




"""Printing example"""
class PrintManager:
    def __init__(self):
        self.queue = Queue()
    
    def queue_print_job(self, document):
        self.queue.enqueue(document)
    
    def run(self):
        # Each time this loop runs, we read the document
        # at the front of the queue:
        while self.queue.read():
            # We dequeue the document and print it:
            self.print_doc(self.queue.dequeue())
    
    def print_doc(self, document):
        # Code to run the actual printer goes here.
        # For demo purposes, we'll print to the terminal:
        print(document)



print_manager = PrintManager()
print_manager.queue_print_job("First Document")
print_manager.queue_print_job("Second Document")
print_manager.queue_print_job("Third Document")
print_manager.run()

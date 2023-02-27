### Chapter 9 [23/Feb/2023] 

Stacks and queues are elegant tools for handling temporary data.

## Stacks
LIFO Last In First Out:this means is that the last item pushed onto astack is always the first item popped from it.
A stack stores data in the same way arrays do. It has three constraints.
• Data can be inserted only at the end of a stack.
• Data can be deleted only from the end of a stack.
• Only the last element of a stack can be read.

most computer science literature refers to the end of the stack as its top, and the beginning of the stack as its bottom.

Inserting a new value into a stack is also called pushing onto the stack.
Removing elements from the top of the stack is called popping from the stack.

## Queues
“FIFO” to queues: First In, First Out.

• Data can be inserted only at the end of a queue. (This is identical behavior to the stack.)
• Data can be deleted only from the front of a queue. (This is the opposite behavior of the stack.)
• Only the element at the front of a queue can be read. (This, too, is the opposite of behavior of the stack.)

inserting into a queue is enqueue
Removing an element from a queue is also known as dequeuing

Queues are also the perfect tool for handling asynchronous requests—they ensure that the requests are processed in the order in which they were received. They are also commonly used to model real-world scenarios where events need to occur in a certain order, such as airplanes waiting for takeoff and patients waiting for their doctor.
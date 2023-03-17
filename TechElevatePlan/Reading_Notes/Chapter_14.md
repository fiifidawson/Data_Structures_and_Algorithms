### Chapter 14 [27/Feb/2023]

## Linked Lists
Connected data that is dispersed throughout memory are known as nodes.They are not contiguous like arrays.
(A linked list’s first node can also be referred to as its head, and its final node as its tail.)

Connected data that is dispersed throughout memory are known as nodes.

(A linked list’s first node can also be referred to as its head, and its final node as its tail.)

When dealing with a linked list, we only have immediate access to its first node.

The four classic operations: reading, searching, insertion, and deletion.

## Reading
To read from the third node, then, the computer must go through a process. First, it accesses the first node(the only node we initially have access to). It then follows the first node’s link to the second node, and then the second node’s link to the third node.
It would take N steps for N nodes in the list. Linked lists having a worst-case read of O(N).

## Searching 
Linked lists also have a search speed of O(N). To search for a value, we need go through a similar process as we did with reading. That is, we begin with the first node and follow the links of each node to the next one.

## Insertion
With insertion at the beginning of the list takes just one step—which is O(1).
If we want to add a new nod to the beginning of the list, all we have to do is create a new node and have its link point to the node next node (previously first node):

In contrast with an array, the linked list provides the flexibility of inserting data to the front of the list without requiring the shifting of any data.
However for a computer to know the preceeding node, it needs to read the nodes up to that point O(N)

Worst case scenario - End of the list, O(N + 1)
Best case scenario - Beginning of the list, O(1)

Scenario                 Array        Linked List
Insert at beginning   Worst case       Best case
Insert at middle     Average case     Average case
Insert at end         Best case        Worst case


## Deletion
To delete a node from the beginning of a linked list, all we need to do is perform one step: we change the first_node of the linked list to now point to the second node.
When it comes to deleting the final node of a linked list, the actual deletion takes one step—we just take the second-to-last node and make its link null. However, it takes N steps to even access the second-to-last node in the first place, since we need to start at the beginning of the list and follow the links until we reach it.

Scenario                 Array        Linked List
Insert at beginning   Worst case       Best case
Insert at middle     Average case     Average case
Insert at end         Best case        Worst case

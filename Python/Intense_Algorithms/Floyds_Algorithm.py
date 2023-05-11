class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    if head is None:
        return False

    tortoise = head  # slow
    hare  = head  # fast

    
    while hare is not None and hare.next is not None:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            return True  # cycle detected

    return False  # no cycle in the list

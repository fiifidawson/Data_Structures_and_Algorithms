### Chapter 3 [13/Feb/2023]  

## Big O
O(N)
Some pronounce this as “Big Oh of N.” Others call it “Order of N.” My personal preference, however, is “Oh of N.”
An algorithm that is O(N) is also known as having linear time.

## O(1) vs O(N)
O(1) represents the performance of an algorithm whose value doesn't irrespective of the number of inputs, the steps remain the same whilst O(N) represents the performance of an whose steps is affected by the number of inputs
An O(1) can take a million steps or just 100 steps but it remains the same. Both might intersect at specific point but O(1) in generally efficient

## Same Algorithm, Different Scenarios
If we were to describe the efficiency of linear search in its totality, we’d say that linear search is 
O(1) ina best-case scenario {Element was found at the first index},
O(N) in a worst-case scenario {Element was found at the last index}.

algorithm, Big O Notation generally refers to the worst-case scenario unless specified otherwise.

## An Algorithm of the Third Kind
In Big O terms, we describe binary search as having a time complexity of:
O(log N). This type of algorithm is also known as having a time complexity of log time.


## O(log N) Explained
Whenever we say O(log N), it’s actually shorthand for saying O(log2N).
Said simply: O(log N) means the algorithm takes as many steps as it takes to keep halving the data elements until we remain with 1.
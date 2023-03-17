### Chapter 2 [12/Feb/2023]

## Order Arrays
The elements in the array are organized in ascending or descending order.
The computer compares the elements in the array to determine where it should be placed.
N+2 or N+1 , searchin, pushing and inserting

## Searching an Ordered Array
Searching an ordered array is different from searching a classic(unoredered array). 
Example
Searching for 20 in a classic array, [17, 3, 75, 202, 80] would meaning we would have to compare each element at each index to the end to check since they are not ordered. But for an ordered array since we know the magnitude of the values, we are positive of its placement.
We can stop early before 75 since we know 22 is greater than 17 but less than 75 [3, 17, 75, 80, 202].

## Binary Search 
This is considered to be the best searching algorithm. The array must be ordered though. It searches an array by taking the midpoint and compares it with the value to be searched. It compares it to the slpit array to determine wether it is greater or less than the left or right hand side and moves to it whilst discarding the other side. This is done repeatedly until the value is found or the value isn't part of the array.

steps = log2(n)


## Binary Search vs Linear Search
Linear search is often suitable for small array sizes.
Taking an example of array with the size 100
Maximum number of steps
- Linear Search: 100
- Binary Search: 50

each time we double the data, the binary search algorithm adds just one more step. For linear search the number steps is the number of elements in the array.

Note:insertion within an ordered array still remains slower than within a regular array, as the regular array’s insertion doesn’t require a search at all.
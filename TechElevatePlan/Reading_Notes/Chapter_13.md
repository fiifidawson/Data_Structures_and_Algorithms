### Chapter 13 [15/June/2023]


## Quick Sort
It is generally used in computers as the most used sorting algorithm. It is very efficient in terms of average case scenarios although it performs equally in terms of worst case scenarios for Insertion and selection sort.
It uses a method called `partitioning`.

## Partioning
It is done by taking a number in an array and using it as a pivot. All numbers less than the pivot are shifted to the left and all numbers greated than the pivot are shifted to the right.

Pointers are assigned to the left most and right most numbers in the array.(Excluding the pivot)

1. The left pointer continuously moves one cell to the right until it reaches
a value that is greater than or equal to the pivot, and then stops.
2. Then, the right pointer continuously moves one cell to the left until it
reaches a value that is less than or equal to the pivot, and then stops.
The right pointer will also stop if it reaches the beginning of the array.
3. Once the right pointer has stopped, we reach a crossroads. If the left
pointer has reached (or gone beyond) the right pointer, we move on to
Step 4. Otherwise, we swap the values that the left and right pointers are
pointing to, and then go back to repeat Steps 1, 2, and 3 again.
4. Finally, we swap the pivot with the value that the left pointer is currently
pointing to.

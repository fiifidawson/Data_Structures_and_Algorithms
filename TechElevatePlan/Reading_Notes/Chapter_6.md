### Chapter 6 [20/Feb/2023]  

## Insertion Sort
Insertion sort starts from the second element or index 1. It stores the value at index 1 in a temporary position. It compares it with the element at the left(index 0) to check wether it is greater or less then it. If the value at index 1 is less than the value to the left, it swaps else it remains there. For subsequent iterations, it moves to the next index and checks all the values to its left and compares to make the necessary swaps. This continues until the loop ends.

Four types of steps occur in Insertion Sort:
- removals (Worst case: Descending order)
- comparisons (1....+.N - 1)(N^2 / 2)
- shifts
- insertions

Worst Case Scenarios
    N^2 / 2 - Comparisons
+   N^2 / 2 - Shifts
----------------------
    N^2 steps


N^2 comparisons and shifts combined
    N - 1 removals
+   N - 1 insertions
_____________________________
N^2 + 2N - 2 steps

Simplify this as O(N^2+ N)

                 Best Case|  Average Case|  Worst Case
Selection Sort - N^2 / 2  |    N^2 / 2   |  N^2 / 2
Insertion Sort -     N    |    N^2 / 2   |  N^2
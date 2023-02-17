### Chapter 4 [15/Feb/2023]  

## Bubble Sort
The Bubble Sort algorithm contains two significant kinds of steps:
• Comparisons: two numbers are compared with one another to determine
which is greater.
• Swaps: two numbers are swapped with one another in order to sort them.

## The Efficiency of Bubble Sort
In a worst-case scenario, where the array is sorted in descending order (the

exact opposite of what we want), we’d actually need a swap for each comparison.
Comparisons and swaps

                |# of Bubble Sort Steps |
N Data Elements |Comparisons|Swaps      |  N^2 
     5          |  10       | 10  = 20  |  25
     10         |  15       | 45  = 90  |  100
     20         |  190      | 190 = 380 |  400
     40         |  780      | 780 = 1560|  1600
     80         |  3160     | 3160= 6320|  6400

Bubble Sort has an efficiency of O(N^2).

## A Quadratic Problem
Very often (but not always), when an algorithm nests one loop inside another, the algorithm is O(N^2). So, whenever you see a nested loop, O(N^2) alarm bells should go off in your head.

## A Linear Solution
Read PDF page 12-14 of Chapter 4. It would literally blow your mind
### Chapter 5 [16/Feb/2023]  

## Selection Sort
We take a value at the first index compare it with all the values in the other indices. If a number less than the value in the first index is encountered, we set the index as the lowest number and continue searching the array for any lower value. We then swap the lowest number in the array to the beginning of the array. We then move on to the second index and perform the same process. Then to the until the end of the array.

We take the indices into consideration

## The Efficiency of Selection Sort
Selection Sort contains two types of steps: comparisons and swaps. That is, we compare each value with the lowest number we’ve encountered in each pass-through, and we swap the lowest number into its correct position.

Here’s a side-by-side comparison of Bubble Sort and Selection Sort:

N Elements |   Max # of Steps   |  Max # of Steps                     |
___________|___in Bubble Sort___|__in Selection Sort__________________|
5          |       20           |   14(10 comparisons + 4 swaps)      |
10         |       90           |   54(45 comparisons + 9 swaps)      |
20         |       380          |   199(180 comparisons + 19 swaps)   |
40         |       1560         |   819(780 comparisons + 39 swaps)   |
80         |       6320         |   3239(3160 comparisons + 79 swaps) |

From this comparison, it’s clear Selection Sort takes about half the number of steps Bubble Sort does, indicating that Selection Sort is twice as fast.

## Ignoring Constants 
In the world of Big O Notation, Selection Sort and Bubble Sort are described in exactly the same way.

Bubble Sort = O(N^2)
Selection Sort = O(N^2/2)

N Elements |    N^2 / 2     | Max # of Steps in Selection Sort 2 
           |                |
     5     | 5^2 / 2 = 12.5 |        14
    10     | 10^2 / 2 = 50  |        54
    20     | 20^2 / 2 = 200 |       199
    40     | 40^2 / 2 = 800 |       819
    80     | 80^2 / 2 = 3200|       3239

In reality, however, Selection Sort is described in Big O as O(N2), just like Bubble Sort. 

This is a major rule of Big O:
Big O Notation ignores constants.
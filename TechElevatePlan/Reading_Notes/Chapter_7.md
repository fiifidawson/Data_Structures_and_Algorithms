### Chapter 7 [21/Feb/2023]  


## Mean Average of Even Numbers
Accepts an array of numbers and returns the
mean average of all its even numbers.Refer to python code.
Time complexity: O(N)
                worst case scenario is when all are even numbers. 
                In the for loop: When simplified it performs three additional steps which are checking whether the numbers are even, adding the even numbers and counting them. This gives us 3N
                Outside for loop: Initializes the two variables to 0 and performs the division of sum / count_of_even_numbers. This gives us 3 additional steps.

Total Steps = 3N + 3

## Word Builder
an algorithm that collects every combination of two-character strings built from an array of single characters. For example, given the array: ["a", "b", "c", "d"], we’d return a new array containing the following
string combinations:
[
'ab', 'ac', 'ad', 'ba', 'bc', 'bd',
'ca', 'cb', 'cd', 'da', 'db', 'dc'
]

Due to the inner for loop, time complexity is O(N^2) for the two-character strings whilst it's O(N^3) for the two inner for loops.
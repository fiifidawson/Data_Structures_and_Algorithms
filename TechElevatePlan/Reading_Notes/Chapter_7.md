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

## Array Sample
We create a function that takes a small sample of an array. We expect to have very large arrays, so our sample is just the first, middlemost, and last value from the array.
O(1)

## Average Celsius Reading
To get the average Celsius temperature, our algorithm does two things: first, it converts all the readings from Fahrenheit to Celsius. Then, it calculates the mean average of all the Celsius numbers.
ALthough there are two for loops, time complexity is N + N (plus some few constant steps) not N^2 since they are not nested.

## Clothing Labels
This code contains nested loops, so it’s tempting to declare this algorithm to be O(N^2). However, we need to analyze this case a little more carefully. While code containing nested loops often is O(N^2), in this case, it’s not. Nested loops that result in O(N^2) occur when each loop revolves around N. In our case, however, while our outer loop runs N times, our inner loop runs a constant five times. That is, this inner loop will always run five times no matter what N is.

Algorithm runs 5N times, this is reduced to O(N)

## Count the Ones
The two loops are iterating over two completely different things. The outer loop is iterating over the inner arrays, and the inner loop is iterating over the actual numbers. At the end of the day, our inner loop only runs for as many numbers as there are in total. Because of this, we can say that N represents how many numbers there are. And since our algorithm simply processes each number, the function’s time complexity is O(N).

## Palindrome Checker
A palindrome is a word or phrase that reads the same both forward and backward.
Big O = N/2 = N

## Get all the Products

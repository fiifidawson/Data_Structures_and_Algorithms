"""
Method 1 [Brute Force]
Compare each number starting from first index to each other one at
a time.
time complexity: O(n^2)
space complexity: O(1)
"""

"""
Method 2 [Sorting]
Duplicates would be adjacent so iterating throught the array would 
be once.
time complexity:
     General: O(nlogn) 
     Sorting: O(n) {sorting - Hash Set/Map}
space complexity:
     General:  O(1)
     Sorting: O(n)
1. First sort
"""
"""
[
[0, 1, 1, 1, 0],
[0, 1, 0, 1, 0, 1],
[1, 0]
]
"""
# Chapter 7
"""Has O(N) time complexity because the inner loop does not depend on the outer loop"""
def count_ones(outer_array):
    count = 0
    for inner_array in outer_array:
        for number in inner_array:
            if number == 1:
                count += 1
    return count
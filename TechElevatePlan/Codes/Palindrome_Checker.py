"""Chapter 7"""


def isPalindrome(string):
    # Start the leftIndex at index 0:
    leftIndex = 0
    # Start rightIndex at last index of array:
    rightIndex = len(string) - 1
    
    # Iterate until leftIndex reaches the middle of the array:
    while leftIndex < len(string) // 2:
        # If the character on the left doesn't equal the character
        # on the right, the string is not a palindrome:
        if string[leftIndex] != string[rightIndex]:
            return False
        # Move leftIndex one to the right:
        leftIndex += 1
        # Move rightIndex one to the left:
        rightIndex -= 1
        
    # If we got through the entire loop without finding any
    # mismatches, the string must be a palindrome:
    return True
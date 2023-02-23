"""Not Optimized O(N^2)"""

def isSubset(array1, array2):
    largerArray = []
    smallerArray = []
    # Determine which array is smaller
    if len(array1) > len(array2):
        largerArray = array1
        smallerArray = array2
    else:
        largerArray = array2
        smallerArray = array1

    # Iterate through smaller array
    for i in range(len(smallerArray)):
        # Assume temporarily that the current value from
        # smaller array is not found in larger array
        foundMatch = False
        
        # For each value in smaller array, iterate through
        # larger array
        for j in range(len(largerArray)):
            # If the two values are equal, it means the current
            # value in smaller array is present in the larger array
            if smallerArray[i] == largerArray[j]:
                foundMatch = True
                break
        
        # If the current value in smaller array doesn't exist
        # in larger array, return false
        if not foundMatch:
            return False

    # If we get to the end of the loops, it means that all
    # values from smaller array are present in larger array
    return True




"""Optimized O(N) 1"""
def isSubset(array1, array2):
    # Create a hashtable to store the elements of the larger array
    hashTable = {}
    for elem in array2:
        hashTable[elem] = True

    # Iterate through the smaller array
    for elem in array1:
        # Check if the current element is in the hashtable
        if elem not in hashTable:
            return False

    # If all elements of the smaller array are present in the hashtable,
    # return True
    return True


"""Optimized O(N) 2"""
def isSubset(array1, array2):
    largerArray = None
    smallerArray = None
    hashTable = {}
    # Determine which array is smaller:
    if len(array1) > len(array2):
        largerArray = array1
        smallerArray = array2
    else:
        largerArray = array2
        smallerArray = array1
    # Store all items from largerArray inside hashTable:
    for value in largerArray:
        hashTable[value] = True
    # Iterate through each item in smallerArray and return false
    # if we encounter an item not inside hashTable:
    for value in smallerArray:
        if value not in hashTable:
            return False
    # If we got this far in our code without returning false,
    # it means that all the items in the smallerArray
    # must be contained within largerArray:
    return True

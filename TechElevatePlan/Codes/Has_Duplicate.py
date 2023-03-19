def hasDuplicateValue(array):
    existingNumbers = []
    for i in range(len(array)):
        if existingNumbers[array[i]] == 1:
            return True
        else:
            existingNumbers[array[i]] = 1
    return False


"""Time Complexity - O(N)
   Space Complexity - O(N)
"""
def has_duplicate_value(array):
    # create an empty dictionary to store existing values
    existing_values = {}
    # loop through the array using a for loop
    for i in range(len(array)):
        # if the current value in the array does not exist in the dictionary
        if not existing_values.get(array[i]):
            # add the current value to the dictionary with a value of True
            existing_values[array[i]] = True
        else:
            # if the current value already exists in the dictionary, return True
            return True
    # if no duplicates are found, return False
    return False

"""Time Complexity - O(logN)
   Space Complexity - O(logN)
"""
def has_duplicate_value(array):
    # sort the array in ascending order
    array.sort()
    # loop through the sorted array
    for i in range(len(array) - 1):
        # if the current element is equal to the next element
        if array[i] == array[i + 1]:
            # return True as a duplicate value is found
            return True
    # if no duplicates are found, return False
    return False

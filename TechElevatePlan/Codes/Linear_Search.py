"Linear Search in an Ordered Array"
def linear_search(array, search_value):
    # Iterate through every element in the array with its index
    for index, element in enumerate(array):
        # If the value we're looking for is found, return its index
        if element == search_value:
            return index
        # If the current element is greater than the value we're looking for, exit the loop
        elif element > search_value:
            break
    # Return None if the value is not found within the array
    return None

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_value = 5

print(linear_search(array, search_value))





"Linear Search in an Unordered Array"
def linear_search(array, search_value):
    # Iterate through every element in the array with its index
    for index, element in enumerate(array):
        # If the value we're looking for is found, return its index
        if element == search_value:
            return index
    # Return None if the value is not found within the array
    return None
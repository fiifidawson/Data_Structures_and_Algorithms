def binary_search(array, search_value):
    # Establish the lower and upper bounds of where the value can be
    lower_bound = 0
    upper_bound = len(array) - 1
    # Keep inspecting the middlemost value between the upper and lower bounds
    while lower_bound <= upper_bound:
        # Find the midpoint between the upper and lower bounds
        midpoint = (upper_bound + lower_bound) // 2
        # Inspect the value at the midpoint
        value_at_midpoint = array[midpoint]
        # Check if the value at the midpoint is the one we're looking for
        if search_value == value_at_midpoint:
            return midpoint
        # Change the lower or upper bound based on the result
        elif search_value < value_at_midpoint:
            upper_bound = midpoint - 1
        elif search_value > value_at_midpoint:
            lower_bound = midpoint + 1
    # Return None if the value is not found within the array
    return None

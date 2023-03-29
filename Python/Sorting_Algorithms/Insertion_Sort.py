def insertion_sort(array):
    # Start an iteration starting from index 1 (second element)
    for index in range(1, len(array)):
        # Store the current element in a temporary variable
        temp_value = array[index]
        # Store the index of the previous element
        # This is the index of the element that we will compare with the temp_value
        position = index - 1 #Decrementing index
        # Loop through the array until we reach the beginning of the array
        while position >= 0:
            # If the current element is greater than the temp_value
            if array[position] > temp_value:
                # Shift the left element to the right
                array[position + 1] = array[position]
                # Decrement the position by 1 
                #to compare the temp_value with the next element
                position = position - 1

            # If the current element is less than the temp_value
            # We have found the correct position for the temp_value
            else:
                break
            # Insert the temp_value into the gap
            array[position + 1] = temp_value
        return array
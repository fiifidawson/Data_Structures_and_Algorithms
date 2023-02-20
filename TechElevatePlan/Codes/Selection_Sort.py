def selection_sort(array):
    # Loop through the array but stop at the second last element
    # since the array would be sorted before the last element
    for i in range(len(array) - 1):
        #Keep track of the index of the lowest number
        lowest_number_index = i
        # Loop through the array starting from the next element to look for the lowest number
        for j in range(i + 1, len(array)):
            # If the current element is less than the lowest number
            if array[j] < array[lowest_number_index]:
                # Update the index of the lowest number
                lowest_number_index = j
        
        # If the lowest number is not the current element
        # If I is already min index you dont want to swap
        if lowest_number_index != i:
            # Swap the current element with the lowest number
            temp = array[i]
            # Swap the lowest number with the current element
            array[i] = array[lowest_number_index]
            # Swap the current element with the lowest number
            array[lowest_number_index] = temp
            # array[i], array[lowest_number_index] = array[lowest_number_index], array[i]
    return array

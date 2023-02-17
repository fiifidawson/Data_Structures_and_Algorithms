"""First Solution"""

def bubble_sort(list):
    # Loop through the list
    for i in range(len(list)):
        # Loop through the list again
        for j in range(len(list)-1):
            # Compare the two elements
            # list[j] = first element 
            # list[j+1] = second element
            # temp = temporary variable
            if list[j] > list[j+1]:
                temp = list[j]
                list[j]= list[j+1] 
                list[j+1] = temp
    return list


list = [10, 5, 3, 7, 2, 1, 9, 8, 6, 4]
print(bubble_sort(list))

"""Second Solution"""

def bubble_sort(list):
    #initialize the unsorted_until_index to the last index of the list
    unsorted_until_index = len(list) - 1

    #sorted to keep track if the list is fully sorted
    # false because we haven't started sorting yet 
    sorted = False
    while not sorted:
        #assume the list is sorted until we encounter a swap then set sorted to false
        # if we don't encounter a swap then the list is sorted 
        sorted = True
        for i in range(unsorted_until_index):
            #compare each pair of adjacent elements
            if list[i] > list[i+1]:
                #swap those values if they’re out of order.
                list[i], list[i+1] = list[i+1], list[i]
                #set sorted to false because we encountered a swap
                sorted = False
        #decrement the unsorted_until_index by 1
        unsorted_until_index -= 1
        
    return list
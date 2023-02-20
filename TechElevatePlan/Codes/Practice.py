#Bubble Sort
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


box = [1, 4, 2, 7, 9, 1]

print(f"Bubble sort {bubble_sort(box)}")

#Selection Sort

def selection_sort(array):
    for i in range(len(array)-1):
        lowest_number_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[lowest_number_index]:
                lowest_number_index = j
        if lowest_number_index != i:
            temp = array[i]
            array[i] = array[lowest_number_index]
            array[lowest_number_index] = temp
    return array


sorted_array = selection_sort(box)
print(f"Selection sort {sorted_array}")


def binary_search(list, searched_value):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high)//2
        if searched_value == list[mid]:
            return mid
        elif searched_value < list[mid]:
            high = mid - 1
            continue
        else:
            low = mid + 1
            continue
    else:
        return -1



searched_value = 9

print(binary_search(sorted_array, searched_value))



# Selection Sort

def SelectionSort(array):
    #Initialising first iteration
    for i in range(len(array)-1):
        #setting the lowest number index
        lowest_number_index = i
        #iterating through unsorted part of the array
        for j in range(i+1, len(array)):
            lowest_number_index = j
        if lowest_number_index != i:
            temp = array[i]
            array[lowest_number_index] = array[i]
            array[i] = temp

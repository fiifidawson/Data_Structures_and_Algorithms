#to write an algorithm that takes an array of numbers and doubles each of the numbers within the array.
def doubleArray(array, index):
    if index >= len(array):
        return

    array[index] += 2
    doubleArray(array, index+1)
        
    


array = [1, 2, 3, 4]
index = 0

print(doubleArray(array, index))
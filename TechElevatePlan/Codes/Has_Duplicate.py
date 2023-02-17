def hasDuplicateValue(array):
    existingNumbers = []
    for i in range(len(array)):
        if existingNumbers[array[i]] == 1:
            return True
        else:
            existingNumbers[array[i]] = 1
    return False
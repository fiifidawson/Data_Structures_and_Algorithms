"""Two Character Strings"""
def wordBuilder(array):
    # Create an empty array to store the combinations
    collection = []

    # Loop through each word in the array
    for i in range(len(array)):
        # Loop through each word in the array again
        for j in range(len(array)):
            # Check that the two words being combined are not the same word
            if i != j:
                # Add the combined word to the collection
                collection.append(array[i] + array[j])

    # Return the collection of combinations
    return collection


"""Three Character Strings"""
def wordBuilder(array):
    # Create an empty array to store the combinations
    collection = []
    # Loop through each word in the array
    for i in range(len(array)):
        # Loop through each word in the array again
        for j in range(len(array)):
            # Loop through each word in the array a third time
            for k in range(len(array)):
                # Check that the three words being combined are all different
                if i != j and j != k and i != k:
                    # Add the combined word to the collection
                    collection.append(array[i] + array[j] + array[k])

    # Return the collection of combinations
    return collection
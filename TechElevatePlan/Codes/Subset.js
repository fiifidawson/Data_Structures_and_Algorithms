"Not Optimized O(N^2)"

function isSubset(array1, array2) {
    let largerArray;
    let smallerArray;
    // Determine which array is smaller:
    if(array1.length > array2.length) {
        largerArray = array1;
        smallerArray = array2;
    } else {
        largerArray = array2;
        smallerArray = array1;
    }
    // Iterate through smaller array:
    for(let i = 0; i < smallerArray.length; i++) {
        // Assume temporarily that the current value from
        // smaller array is not found in larger array:
        let foundMatch = false;
    
        // For each value in smaller array, iterate through
        // larger array:
        for(let j = 0; j < largerArray.length; j++) {
            // If the two values are equal, it means the current
            // value in smaller array is present in the larger array:
            if(smallerArray[i] === largerArray[j]) {
                foundMatch = true;
                break;
            }
        }
        // If the current value in smaller array doesn't exist
        // in larger array, return false:
        if(foundMatch === false) { return false; }
    }
    // If we get to the end of the loops, it means that all
    // values from smaller array are present in larger array:
    return true;
}

"Optimized O(N)"
function isSubset(array1, array2) {
    let largerArray;
    let smallerArray;
    let hashTable = {};
    // Determine which array is smaller:
    if(array1.length > array2.length) {
        largerArray = array1;
        smallerArray = array2;
    } else {
        largerArray = array2;
        smallerArray = array1;
    }
    // Store all items from largerArray inside hashTable:
    for(const value of largerArray) {
        hashTable[value] = true;
    }
    // Iterate through each item in smallerArray and return false
    // if we encounter an item not inside hashTable:
    for(const value of smallerArray) {
        if(!hashTable[value]) { return false; }
    }

    // If we got this far in our code without returning false,
    // it means that all the items in the smallerArray
    // must be contained within largerArray:
    return true;
}

"Quadratic Time Complexity O(n^2)"
function hasDuplicateValue(array) {
    let steps = 0; // count of steps
    for(let i = 0; i < array.length; i++) {
        for(let j = 0; j < array.length; j++) {
            steps++; // increment number of steps
            if(i !== j && array[i] === array[j]) {
                return true;
            }
        }
    }
    console.log(steps); // print number of steps if no duplicates
    return false;
}

"Linear Time Complexity O(n)"
function hasDuplicateValue(array) {
    // create an empty array to store the numbers we've seen
    let existingNumbers = [];
    // Use a loop to check each number in the array
    for(let i = 0; i < array.length; i++) {
        // if the number is already in the array, return true
        // === 1 is used to check if the number is in the array
        // As it encounters each
        // number, it places an arbitrary value (we’ve chosen to use a 1) in the existingNumbers
        // array at the index of the number we’re encountering.
        if(existingNumbers[array[i]] === 1) {
            return true;
        } else {
            existingNumbers[array[i]] = 1;
        }
    }
    return false;
}
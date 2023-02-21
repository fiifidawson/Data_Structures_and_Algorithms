"Chapter 7"

function isPalindrome(string) {
    // Start the leftIndex at index 0:
    let leftIndex = 0;
    // Start rightIndex at last index of array:
    let rightIndex = string.length - 1;
    // Iterate until leftIndex reaches the middle of the array:
    while (leftIndex < string.length / 2) {
    // If the character on the left doesn't equal the character
    // on the right, the string is not a palindrome:
        if (string[leftIndex] !== string[rightIndex]) {
            return false;
        }
        // Move leftIndex one to the right:
        leftIndex++;
        // Move rightIndex one to the left:
        rightIndex--;
        }
        // If we got through the entire loop without finding any
        // mismatches, the string must be a palindrome:
    return
}
# Data_Structures_and_Algorithms
Practice for DSA

### Chapter 1 [9/Feb/2023]  
## Measuring Speed 
Measuring the speed of an algorithm is based on the number steps taken, not the (pure) time taken to execute the alogrithm 

## Reading
This invovles asking the computer to provide information on a data stored in a specific memory slot by providing the index of the array to the computer. The index of an array is in increasing order of 1 to the memory address.

## Searching
This invovles providing the computer with a value of data stored in an array and asking for the index. It's a bit more complex and resource demanding than with Reading.
It tkaes N number of steps to linear search an array.

## Inserting
Inserting an element at the end of an array only takes on step. The computer already knows the size of the array so increments it by one to create room for new data.
It is different when insert at any position or at the beginning of the array since extra steps would be required to shift the other elements. 
Worst case scenario is inserting an element at the beginning 
[We can say that insertion in a worst-case scenario can take N + 1 steps for
an array containing N elements. This is because we need to shift all N elements
over, and then finally execute the actual insertion step].

## Deletion
It is similar to insertion, we need to make room for spaces in the array. The worst case scenario is deleting an element at the beginning of an array
[We can say then, that for an array containing N elements, the maximum number of steps that deletion would take is N steps.]

## Sets
Sets do not allow dublicate data. Reading and Searching in a set is the same for an array. Inserting on the other hand is a bit different. The set first needs to be search to ensure that there's no similar element existing in the array before placing the element in there. So it takes N + 1 number of steps.
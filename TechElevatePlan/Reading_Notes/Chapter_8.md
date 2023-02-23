### Chapter 8 [23/Feb/2023] 

## Hash Map
Extremely fast look ups. O(1)
Other names include hashes, maps, hash maps, dictionaries, and associative arrays.

A hash table is a list of paired values. The first item in each pair is called the key, and the second item is called the value.

HashTable = {Key/Index: Value}

Looking up a value in a hash table has an efficiency of O(1) on average, 2as it usually takes just one step.

## Hashing and Hash Function
A = 1
B = 2
C = 3
D = 4
E = 5

The process of taking characters and converting them to numbers is known as hashing.

The code that is used to convert those letters into particular numbers is called a hash function.

Placement of a value is determined by its key.

Searching
Unordered Array = O(N)
Ordered Array = O(logN)
Hash Map = O(1)

## One-Directional Lookups
It’s important to point out that the ability to find any value within the hash table in a single step only works if we know the value’s key.

If, on the other hand, we want to use a value to find its associated key, we cannot take advantage of the hash table’s fast lookup ability.
we use the key to find the value. The value does not determine the key’s location

## Dealing with Collisions
Trying to add data to a cell that is already filled is known as a collision.
separate chaining: When a collision occurs, instead of placing a single value in the cell, it places in it a reference to an array.

## Making an Efficient Hash Table
Ultimately, a hash table’s efficiency depends on three factors:
• How much data we’re storing in the hash table
• How many cells are available in the hash table
• Which hash function we’re using

A good hash function, therefore, is one that distributes its data across all available cells. The more we can spread out our data, the fewer collisions we will have.

## The Great Balancing Act
A good hash tablestrikes a balance of avoiding collisions while not consuming lots of memory.
This ratio of data to cells is called the load factor. Using this terminology, we’d say that the ideal load factor is 0.7 (7 elements / 10 cells).
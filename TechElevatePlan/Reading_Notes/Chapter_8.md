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
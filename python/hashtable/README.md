# Hashtables

Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

## Challenge

Implement a Hashtable Class with the following methods:

add
get
contains
hash

## Approach & Efficiency

+ creating a Hashtable class, with the init function to take the size parameter, in order to create proper buckets for the keys/values to be stored.

+ then we have the add contains method, that checks if the key is inside the Hashtable,

+ the add method is for adding value to the Hashtable
+ get method is for retrieving the value for a key when inserted, and returns a None if the key does not exist
+ hash, which simply hashes the key, and return the index of where should this key/value pair should be saved at.
+ Time complexity: O(1), it provides a constant and instantaneous results, because we know exactly the index of where to look

+ Space complexity: O(n), we are creating an array with a size of n, in order to store the key/value pairs

## API

add: This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

get: Returns a value associated with that key in the table if exist

contains: Returns a boolean, indicating if the key exists in the table already.

hash: Returns the Index in the collection for that key


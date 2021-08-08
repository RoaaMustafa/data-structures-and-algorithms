# stack and Queueu

stack is like a container that work as (LIFO) last in first out

queueu is like a container that work as (FIFO) first in first out

## Challenge

Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
Create a Queue class that has a front property. It creates an empty Queue when instantiated.

## Approach & Efficiency

+ Implemented both data structures ( stack and  queue) using a basic node class with a next and a value set to none

+ Sstack: I created a class '''Stack()''' and initialized it with self and top properties then do the other methods in the class

+ Queue: I created a class '''Queue()''' and initialized it with self and front and rear properties ten i do the other methods in this class

+ Big O for space and time is O (1)

## API

### Stack

**push:**
Arguments: value
adds a new node with that value to the top of the stack with an O(1) Time performance.
**pop:**
Arguments: none
Returns: the value from node from the top of the stack
Removes the node from the top of the stack
Should raise exception when called on empty stack
**peek:**
Arguments: none
Returns: Value of the node located at the top of the stack
Should raise exception when called on empty stack
**is empty:**
Arguments: none
Returns: Boolean indicating whether or not the stack is empty.

### Queue

**enqueue:**
Arguments: value
adds a new node with that value to the back of the queue with an O(1) Time performance.
**dequeue:**
Arguments: none
Returns: the value from node from the front of the queue
Removes the node from the front of the queue
Should raise exception when called on empty queue
**peek:**
Arguments: none
Returns: Value of the node located at the front of the queue
Should raise exception when called on empty stack
**is empty:**
Arguments: none
Returns: Boolean indicating whether or not the queue is empty

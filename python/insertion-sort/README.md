# Insertion Sort

Create function take an array as argument than sort it in Insertion Sort.
Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

## Whiteboard Process

![insertion-sort](whiteboard/insertion_sort.jpg)

## Approach & Efficiency

+ Define function take list.
+ for loop in range (1,len(arr))
+ while loop let j = i-1 and temp = arr[i]
+ decleare another loop while j more than or equal zero and temp less than arr[j]
+ if true arr[j+1]=arr[j] and j=j-1
+ after while loop breake let arr[j+1]=temp
+ after for loop breake return the list
+ Time: O(n^2)
+ Space: O(1)

## Solution

```
def InsertionSort(arr):

  for i in range(1,len(arr)):

    j=i-1
    temp=arr[i] # 16

    while j >=0 and temp < arr[j]: # 2>0 and 16 < 23
      arr[j+1]=arr[j]
      j=j-1

    arr[j + 1] =temp #

  return arr
```

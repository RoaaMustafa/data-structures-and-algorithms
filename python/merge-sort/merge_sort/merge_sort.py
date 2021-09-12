
def Mergesort(arr):
  n=len(arr)

  if n > 1:

    mid = n//2
    left = arr[0:mid]
    right = arr[mid:n]

    Mergesort(left)
    Mergesort(right)
    Merge(left, right, arr)

  return arr

def Merge(left, right, arr):
  i=0
  j=0
  k=0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      arr[k] = left[i]
      i=i+1
    else:
      arr[k]=right[j]
      j=j+1

    k=k+1

  while i < len(left):
    arr[k] = left[i]
    i += 1
    k += 1

  while j < len(right):
    arr[k] = right[j]
    j += 1
    k += 1



# //////////////////////////////////

arr=[8,4,23,42,16,15]
print(f' array: {arr}')
Mergesort(arr)
print(f'sorted : {arr}')

reversed_arr=[20,18,12,8,5,-2]
print(f' array: {reversed_arr}')
Mergesort(reversed_arr)
print(f'sorted : {reversed_arr}')
Few_uniques=[5,12,7,5,5,7]
print(f'array : {Few_uniques}')
Mergesort(Few_uniques)
print(f'sorted : {Few_uniques}')
Nearly_sorted=[2,3,5,7,13,11]
print(f'array : {Nearly_sorted}')
Mergesort(Nearly_sorted)
print(f'sorted : {Nearly_sorted}')



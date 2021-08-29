def insertionSort(arr):

  for i in range(1,len(arr)):

    j=i-1
    temp=arr[i]

    while j >=0 and temp < arr[j]:
      arr[j+1]=arr[j]
      j=j-1

    arr[j + 1] =temp

  return arr


arr=[8,4,23,42,16,15]
reversed_arr=[20,18,12,8,5,-2]
Few_uniques=[5,12,7,5,5,7]
Nearly_sorted=[2,3,5,7,13,11]
print(f'{arr}---->{insertionSort(arr)}')
print(f'{reversed_arr}---->{insertionSort(reversed_arr)}')
print(f'{Few_uniques}---->{insertionSort(Few_uniques)}')
print(f'{Nearly_sorted}---->{insertionSort(Nearly_sorted)}')

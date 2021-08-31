def QuickSort(arr, left, right):
    if left < right:

        position = Partition(arr, left, right)

        QuickSort(arr, left, position - 1)

        QuickSort(arr, position + 1, right)

    return arr
def Partition(arr, left, right):

    pivot = arr[right]
    low = left - 1

    for i  in range(left,right):

        if arr[i] <= pivot :

            low += 1
            Swap(arr, i, low)

    Swap(arr, right, low + 1)

    return low + 1


def Swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
# ////////////////////////////////////////////////////
arr=[8,4,23,42,16,15]
print(f' array: {arr}')
QuickSort(arr,0,5)
print(f'sorted : {arr}')

reversed_arr=[20,18,12,8,5,-2]
print(f' array: {reversed_arr}')
QuickSort(reversed_arr,0,5)
print(f'sorted : {reversed_arr}')
Few_uniques=[5,12,7,5,5,7]
print(f'array : {Few_uniques}')
QuickSort(Few_uniques,0,5)
print(f'sorted : {Few_uniques}')
Nearly_sorted=[2,3,5,7,13,11]
print(f'array : {Nearly_sorted}')
QuickSort(Nearly_sorted,0,5)
print(f'sorted : {Nearly_sorted}')

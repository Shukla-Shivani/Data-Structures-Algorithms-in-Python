"""Implement merge sort in Python.
Input a list.
Output a sorted list."""

"function to merge two sub arrays"
def merge(left, right, array):
    i = 0
    j = 0
    k = 0
    mergeSort(left)
    mergeSort(right)

    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1

    while (i < len(left)):
        array[k] = left[i]
        i = i + 1
        k = k + 1

    while (j < len(right)):
        array[k] = right[j]
        j = j + 1
        k = k + 1

"function to divide and merge input array"
def mergeSort(array):

    n = len(array)
    mid = n//2
    left = []
    right = []

    for i in range(mid):
        number = array[i]
        left.append(number)

    for i in range(mid, n):
        number = array[i]
        right.append(number)

#mergeSort(left)
#mergeSort(right)
    merge(left, right, array)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
mergeSort(test)
for i in test:
    print(i)

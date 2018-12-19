"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(array, low, high):

    i = low - 1 #index of smaller element
    pivot = array[high] #pivot element

    for j in range(low, high):

        if array[j] <= pivot: #if current element smaller or equal to pivot
            i = i + 1 #increment index of smaller element
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1


def quickSort(array):
    quickSortHelper(array, 0, len(array)-1)
    return array


def quickSortHelper(array, low, high):

    if low < high:

        pi = partition(array, low, high) #partitioning index, array[p] is at right place
        #sort elements before and after parition
        quickSortHelper(array, low, pi-1)
        quickSortHelper(array, pi+1, high)

"Test cases"
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test1 = [10, 7, 8, 9, 1, 5]
print(quickSort(test))
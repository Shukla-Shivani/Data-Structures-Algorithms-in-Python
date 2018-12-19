"""Implement merge sort in Python.
Input a list.
Output a sorted list."""

def mergeSort(array):
    if len(array)>1:
        mid = len(array) // 2
        L = array[:mid]
        R = array[mid:]

        mergeSort(L)
        mergeSort(R)

        i = 0
        j = 0
        k = 0

        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                array[k] = L[i]
                i = i+1
            else:
                array[k] = R[j]
                j = j+1
            k = k+1

        while i<len(L):
            array[k] = L[i]
            i = i+1
            k = k+1

        while j<len(R):
            array[k] = R[j]
            j = j+1
            k = k+1

    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(mergeSort(test))


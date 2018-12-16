"""Binary Search
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    length = len(input_array)
    mid = length/2
    if value<=mid:
        for i in range(0, mid):
            if value == input_array[i]:
                return i
    elif value>=mid+1:
        for i in range(mid+1,length):
            if value == input_array[i]:
                return i
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)

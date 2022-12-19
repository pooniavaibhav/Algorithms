"""
You get a sorted list.
Find an element in the given list using binary search.
"""

#A = [1, 2, 3, 4, 5, 6, 7]
A = [11, 12, 13, 14, 15, 16, 17]
elem = 17

def binary_search(A,elem):

    last_elem_index = len(A) - 1
    start_elem_index = 0
    while start_elem_index <= last_elem_index:
        mid_index = (start_elem_index + last_elem_index) // 2
        mid_value = A[mid_index]
        if mid_value == elem:
            return mid_index
        else:
            if elem < mid_value:
                last_elem_index = mid_index - 1
            else:
                start_elem_index = mid_index + 1
    return -1

result = binary_search(A, elem)
print(result)
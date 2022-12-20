"""
Sort a list using Bubble sort algorithm.
"""

def bubble_sort(input_list):
    for i in range(len(input_list)-1):
        for ind in range(len(input_list) - i - 1):
            if input_list[ind] >= input_list[ind + 1]:
                input_list[ind], input_list[ind + 1] = input_list[ind+1], input_list[ind]
    return input_list


X = [2, 5, 3, 3, 8, 10, 4]

print(bubble_sort(X))
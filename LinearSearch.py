"""
Q - Find the index of an element from a given list.
a = [4,5,8,10,11,6,2,1]
target = 10
return index value 3 if found else -1.
"""

def search(input_list,elem):
    for i, j in enumerate(input_list):
        if j == elem:
            return i
    return -1



result = search([4,5,8,10,11,6,2,1],1)

print(result)
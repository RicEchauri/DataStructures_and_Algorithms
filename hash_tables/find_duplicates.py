"""
HT: Find Duplicates ( ** Interview Question)
find_duplicates()
Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).
Input:
    A list of integers nums.
Output:
    A list of integers representing the numbers in the input array nums that appear more than once. If no duplicates are found in the input array, return an empty list [].
"""

def find_duplicates(input_list):
    my_dict = {}
    output_list = []
    for item in input_list:
        if item in my_dict:
            output_list.append(item)
        else:
            my_dict[item] = True
    return output_list

print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""
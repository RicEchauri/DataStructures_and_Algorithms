"""
Set: Find Pairs ( ** Interview Question)
You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.
Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs.  Assume that each array does not contain duplicate values.
The tests for this exercise assume that arr1 is the list being converted to a set.
Input
Your function should take in the following inputs:
    arr1: a list of integers
    arr2: a list of integers
    target: an integer
Output
Your function should return a list of tuples, where each tuple contains two integers from arr1 and arr2 that add up to target.
"""

def find_pairs(list1, list2, target):
    dir_2 = {}
    output = []
    for value in list2:
        dir_2[value] = True
    for value in list1:
        if (target - value) in dir_2:
            output.append((value, (target - value)))
    return output

"""
def find_pairs(arr1, arr2, target):
    # Convert arr1 to a set for O(1) lookup
    set1 = set(arr1)
    # Initialize an empty list to store the pairs
    pairs = []
    # Loop through each number in arr2
    for num in arr2:
        # Calculate the complement of the current number
        complement = target - num
        # Check if the complement is in set1
        if complement in set1:
            # If it is, add the pair to the pairs list
            pairs.append((complement, num))
    # Return the list of pairs that add up to the target value
    return pairs

"""

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""

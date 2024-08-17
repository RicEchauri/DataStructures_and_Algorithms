"""
Set: Longest Consecutive Sequence ( ** Interview Question)
Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).
Use sets to optimize the runtime of your solution.
Input: An unsorted array of integers, nums.
Output: An integer representing the length of the longest consecutive sequence in nums.
"""
def longest_consecutive_sequence(arr):
    set1 = set(arr)
    temp = set()
    max_len = 0
    temp.add()
    for data in set1:
        if ((data - 1) in temp) or ((data + 1) in temp) :
            temp.add(data)
        if len(temp) > max_len:
            max_len = len(temp)
            temp = set()
    return max_len
    
    
print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
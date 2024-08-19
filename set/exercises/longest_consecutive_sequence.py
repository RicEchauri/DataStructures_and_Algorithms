"""
Set: Longest Consecutive Sequence ( ** Interview Question)
Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).
Use sets to optimize the runtime of your solution.
Input: An unsorted array of integers, nums.
Output: An integer representing the length of the longest consecutive sequence in nums.
"""
def longest_consecutive_sequence(arr):
    set1 = set(arr)  
    n_max = 0
    c_n = 0
    selec = 1
    for data in (set1):
        c_n = 1
        if ((data - 1) in set1):
            selec = -1
        elif ((data + 1) in set1):
            selec = +1
        else:
            n_max = max(n_max, c_n)
            continue
        
        c_data = data
        while c_data + selec in set1:
            c_n += 1
            c_data += selec
            
        n_max = max(n_max, c_n)
    return n_max

"""
def longest_consecutive_sequence(nums):
    # First, the function creates a set called num_set that contains all 
    # the elements of nums. Creating a set from the array allows the function 
    # to check whether an element is in the array in constant time, 
    # which optimizes the runtime of the solution.
    num_set = set(nums) 
    
    # The function initializes the variable longest_sequence to zero, 
    # which will be updated as the function finds longer sequences.
    longest_sequence = 0
    
    # Next, the function loops through each number in the nums array. 
    # For each number, it checks if the previous number is not in num_set, 
    # which means the current number is the start of a new sequence. 
    for num in nums:
    
    # If the previous number is not in num_set, the function initializes a 
    # variable current_num to the current number and a variable current_sequence 
    # to 1, since the current number is the first element of a new sequence.
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1
            
            # The function then loops through the remaining elements of the sequence, 
            # incrementing the current_num and current_sequence variables for each element 
            # that is one more than the previous element. This loop stops when the next 
            # element is not in num_set, which means the sequence has ended.
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
            
            # Once the loop has ended, the function updates the longest_sequence variable 
            # to the maximum of its current value and the current_sequence value, since 
            # current_sequence represents the length of the sequence that has just been found.
            longest_sequence = max(longest_sequence, current_sequence)
    
    return longest_sequence
"""
    
    
print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )
print( longest_consecutive_sequence([100, 99, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
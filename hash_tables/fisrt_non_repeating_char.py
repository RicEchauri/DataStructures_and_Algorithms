"""
HT: First Non-Repeating Character ( ** Interview Question)
You have been given a string of lowercase letters.
Write a function called first_non_repeating_char(string) that finds the first non-repeating character 
in the given string using a hash table (dictionary). If there is no non-repeating character in the string, 
the function should return None.
For example, if the input string is "leetcode", the function should return "l" because "l" is the first 
character that appears only once in the string. Similarly, if the input string is "hello", the function 
should return "h" because "h" is the first non-repeating character in the string.
"""

def first_non_repeating_char(input_string):
    my_dict = {}
    for key in input_string:
        if key in my_dict:
            my_dict[key] = False
        else:
            my_dict[key] = True
    for char in input_string:
        if my_dict[char]:
            return char
    return None
"""
def first_non_repeating_char(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in string:
        if char_counts[char] == 1:
            return char
    return None
"""
print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
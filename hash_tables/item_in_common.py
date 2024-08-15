"""
HT: Item In Common ( ** Interview Question)
Write a function item_in_common(list1, list2) that takes two lists as input and returns True if there is at least one common item between the two lists, False otherwise.
Use a dictionary to solve the problem that creates an O(n) time complexity.
"""

def item_in_common(list1, list2) -> bool:
    my_dict = {}
    for item in list1:
        my_dict[item] = True
    for key in list2:
        if key in my_dict:
            return True
    return False

list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""
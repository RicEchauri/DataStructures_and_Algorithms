"""
LL: Reverse Between ( ** Interview Question)
You are given a singly linked list and two integers start_index and end_index.
Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from start_index to  end_index (inclusive using 0-based indexing) in one pass and in-place.
Note: the Linked List does not have a tail which will make the implementation easier.
Assumption: You can assume that start_index and end_index are not out of bounds.
Input
    The method reverse_between takes two integer inputs start_index and end_index.
    The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds)
Output
    The method should modify the linked list in-place by reversing the nodes from start_index to  end_index.
    If the linked list is empty or has only one node, the method should return None. 
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
    # def reverse_between(self, start_index, end_index):
    #     pre = self.head
    #     temp = self.head
    #     for _ in range(start_index):
    #         pre = temp
    #         temp = temp.next
    #     after = temp.next
    #     before = None
    #     for _ in range(end_index - start_index + 1):
    #         after = temp.next
    #         temp.next = before
    #         before = temp
    #         temp = after
    #     pre.next = before
        
    def reverse_between(self, start_index, end_index):
        temp = self.head
        pre = None
        for _ in range(start_index):
            pre = temp
            temp = temp.next
        after = temp.next
        before = None
        head = temp
        for _ in range(end_index - start_index + 1):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        if pre:
            pre.next = before
        else:
            self.head = before
        head.next = after
        
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# # Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
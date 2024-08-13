class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        temp = [0] * (len(self.stack_list) - 1)
        node = None
        if len(self.stack_list) != 0:
            node = self.stack_list[len(self.stack_list) - 1]
        for index in range(len(self.stack_list) - 1):
            temp[index] = self.stack_list[index]
        self.stack_list = temp
        return node
"""
Stack: Parentheses Balanced ( ** Interview Question)
Check to see if a string of parentheses is balanced or not.
By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.
Your program should take a string of parentheses as input and return True if it is balanced, or False if it is not. In order to solve this problem, use a Stack data structure.
Function name:
is_balanced_parentheses
Remember: this is not a method within the Stack class, this is a separate function.  Indent all the way to the left.
"""
def is_balanced_parentheses(str_p):
    if len(str_p) % 2:
        return False
    pair = 0
    for data in str_p:
        if data == "(" :
            pair += 1
        if data == ")":
            pair -= 1
    return pair == 0


"""
Stack: Reverse String ( ** Interview Question)
The reverse_string function takes a single parameter string, which is the string you want to reverse.
Return a new string with the letters in reverse order.
"""
def reverse_string(str_in):
    return str_in[::-1]

"""
Stack: Sort Stack ( ** Interview Question)
The sort_stack function takes a single argument, a Stack object.  The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack. 
The function should use the pop, push, peek, and is_empty methods of the Stack object.
Note: This is a new function, not a method within the Stack class. So, your indent should be all the way to the LEFT.
"""
def sort_stack(input_stack):
    sorted_stack = Stack()
    while not input_stack.is_empty():
        temp = input_stack.stack_list.pop()
        while (not sorted_stack.is_empty()) and (sorted_stack.peek() > temp):
            input_stack.push(sorted_stack.pop())
        sorted_stack.push(temp)
            
    while not sorted_stack.is_empty():
        input_stack.push(sorted_stack.pop())
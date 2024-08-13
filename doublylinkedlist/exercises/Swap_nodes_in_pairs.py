"""
DLL: Swap Nodes in Pairs ( ** Interview Question)
You are given a doubly linked list.
Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list. The method should not take any input parameters.
Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp
    
    def swap_pairs(self):
        if not self.head or not self.head.next:
            return False
        temp = self.head
        self.head = temp.next
        while temp and temp.next:
            head1 = temp.prev
            head2 = temp.next.next
            temp.next.prev = head1
            if head1:
                head1.next = temp.next
            temp.next.next = temp
            temp.prev = temp.next
            temp.next = head2
            if head2:
                head2.prev = temp
            
            temp = temp.next
        
        return True
    
    """
            def swap_pairs(self):
            dummy_node = Node(0)
            dummy_node.next = self.head
            previous_node = dummy_node
        
            while self.head and self.head.next:
                first_node = self.head
                second_node = self.head.next
        
                previous_node.next = second_node
                first_node.next = second_node.next
                second_node.next = first_node
        
                second_node.prev = previous_node
                first_node.prev = second_node
        
                if first_node.next:
                    first_node.next.prev = first_node
        
                self.head = first_node.next
                previous_node = first_node
        
            self.head = dummy_node.next
        
            if self.head:
                self.head.prev = None
    """

my_dll = DoublyLinkedList(1)
my_dll.pop_first()
# my_dll.append(2)
# my_dll.append(3)
# my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""
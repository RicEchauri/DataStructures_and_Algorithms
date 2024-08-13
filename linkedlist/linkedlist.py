class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

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
    
    def find_middle_node(self):
        """
        INITIALIZE slow and fast pointers to head of the linked list
        WHILE fast is not None and fast.next is not None: MOVE slow pointer one step (slow = slow.next) MOVE fast pointer two steps (fast = fast.next.next)
        RETURN slow pointer (middle node of the linked list) 
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def has_loop(self):
        """
        initialize slow and fast pointers to head of the list
        while fast is not None and fast.next is not None:
        move slow pointer one step forward
        move fast pointer two steps forward
        if slow and fast pointers are equal:
            return True (loop found)
        return False (loop not found)
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def find_kth_from_end(l_list, k):
        """
        initialize slow and fast pointers to the head of the linked list
        for i in range k:
            if fast pointer is None:
                return None (list is shorter than k)
            move fast pointer to the next node
        while fast pointer is not None:
            move slow pointer to the next node
            move fast pointer to the next node
        return the slow pointer (k-th node from the end)
        """
        fast = l_list.head
        slow = l_list.head
        for _ in range(k):
                if fast is None:
                    return None
                fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
    
    def partition_list(self, x):
        """
        Implement the partition_list member function for the LinkedList class, 
        which partitions the list such that all nodes with values less than x 
        come before nodes with values greater than or equal to x.
        """
        if self.head:
            temp = self.head
            first_half = None
            first_head = None
            second_half = None
            second_head = None
            while temp:
                print(temp.value)
                if temp.value < x and not first_half:
                    print("create first_half")
                    first_half = Node(temp.value)
                    first_head = first_half
                    print("first_half.value =",first_half.value)
                elif temp.value < x:
                    first_half.next = Node(temp.value)
                    first_half = first_half.next
                    print("add node to fist=", first_half.value)
                elif not second_half:
                    print("create second_half")
                    second_half = Node(temp.value)
                    second_head = second_half
                    print("second_half.value =",second_half.value)
                else:
                    second_half.next = Node(temp.value)
                    second_half = second_half.next  
                    print("add node to second=", second_half.value)
                if temp.next is None and first_half:
                    first_half.next = second_head    
                temp = temp.next
            if not first_head:
                first_head = second_head
            self.head = first_head
            
    def remove_duplicates(self):
        temp = self.head
        pre = self.head
        vals = []
        while temp and temp.next:
            if temp.value in vals:
                temp = temp.next.next
                pre.next = temp
            else:
                vals.append(temp.value)
                temp = temp.next
                pre.next = temp
                
    def binary_to_decimal(self):
        temp = self.head
        pos = self.length - 1
        x = 0
        while temp:
            x += temp.value * (2**pos)
            pos -= 1
            temp = temp.next
        return x
    
    def make_empty(self):
        self.head = None
        self.length = 0
            
    def reverse_between(self, start_index, end_index):
        #print("Start reverse_between")
        temp = self.head
        pre = None
        for _ in range(start_index):
            pre = temp
            temp = temp.next
        after = temp.next
        before = None
        head = temp
        for _ in range(end_index - start_index + 1):
            # print("temp", temp.value)
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        if pre:
            pre.next = before
        else:
            self.head = before
        head.next = after
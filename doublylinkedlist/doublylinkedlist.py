class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index <= (self.length / 2):
            for _ in range(index):
                temp = temp.next
        else: 
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev    
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
        temp = self.get(index)
        temp.prev.next = new_node
        new_node.next = temp
        new_node.prev = temp.prev
        temp.prev = new_node
        self.length += 1
        return True
    
    """
    insert option 2
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1   
        return True  
    """
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
    def swap_first_last(self):
        if not self.head:
            return False
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp
        return True
    """
    def swap_first_last(self):
        if self.head is None or self.head == self.tail:
            return
        self.head.value, self.tail.value = self.tail.value, self.head.value
    """
    def reverse(self):
        if self.head == None:
            return False
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        before = None
        next = temp.next
        while temp:
            next = temp.next
            temp.prev = next
            temp.next = before
            before = temp
            temp = next
        return True
    
    """
    def reverse(self):
        temp = self.head
        while temp is not None:
            # swap the prev and next pointers of node points to
            temp.prev, temp.next = temp.next, temp.prev
            
            # move to the next node
            temp = temp.prev
            
        # swap the head and tail pointers
        self.head, self.tail = self.tail, self.head
    """
    
    def is_palindrome(self):
        if self.head == None:
            return True
        first = self.head
        second = self.tail
        
        for _ in range(self.length // 2):
            if first.value != second.value:
                return False
            first = first.next
            second = second.prev
            
        return True
    
    """
        def is_palindrome(self):
        if self.head == None:
            return True
            
        slow = self.head
        fast = slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        first = slow
        second = slow
        
        while first and second:
            if first.value != second.value:
                return False
            first = first.prev
            second = second.next
            
        return True
    """
    
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
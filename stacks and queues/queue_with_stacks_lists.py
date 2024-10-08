class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
        
    def enqueue(self, value):
        while not self.is_empty():  
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        for _ in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
            
    def dequeue(self):
        if not len(self.stack1): return None
        temp = self.stack1.pop()
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        print(temp)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return temp
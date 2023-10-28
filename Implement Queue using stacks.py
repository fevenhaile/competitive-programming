class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2:  # If stack2 is empty, transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        popped = self.stack2.pop() if self.stack2 else None  # Pop element from stack2 if it is not empty
        return popped

    def peek(self):
        if not self.stack2:  # If stack2 is empty, transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        peeked = self.stack2[-1] if self.stack2 else None  # Get the top element from stack2 if it is not empty
        return peeked

    def empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0


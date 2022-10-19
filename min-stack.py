# Design a stack that supports push, pop, top, and retrieving the minimum element in   constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


class MinStack(list):
    def push(self, x):
        self.append((x, min(x, self.getMin())))

    def pop(self):
        return super().pop()[0]

    def top(self):
        return self[-1][0]

    def getMin(self):
        return self[-1][1] if self else inf

class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        i=0
        while i<n:
            y=x+y
            x, y=y, x
            i+=1
        return x

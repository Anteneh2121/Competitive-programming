class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        m = 10**9 + 7
        n = pow(2,p) - 1
        return (pow(n - 1,(n - 1)//2,m) % m * n) % m

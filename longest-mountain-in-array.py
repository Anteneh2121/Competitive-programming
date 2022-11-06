class Solution:
    def longestMountain(self, A: List[int]) -> int:
        ans, start = 0, None
        for i in range(1, len(A)):
            if A[i] > A[i-1] and (i == 1 or A[i-1] <= A[i-2]):
                start = i - 1
            elif A[i] == A[i-1]:
                start = None 
            elif A[i] < A[i-1] and start is not None:
                ans = max(ans, i - start + 1)
        return ans

from functools import lru_cache

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        @lru_cache(None)
        def dfs(i, k, t):
            if k == 0 and t == 0:
                    return 1
            if k == 0 and t != 0 or i == len(arr):
                return 0
            return (dfs(i+1, k, t) + (dfs(i+1, k-1, t-arr[i]) if t >= arr[i] else 0))%(10**9+7)
        return dfs(0, 3, target)    
    

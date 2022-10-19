#reduce-array-size-to-the-half
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        freq = sorted(d.values(), reverse=True)
        cur = 0
        n = 0
        for f in freq:
            cur += f
            n += 1
            if cur >= len(arr) // 2:
                return n
        
        

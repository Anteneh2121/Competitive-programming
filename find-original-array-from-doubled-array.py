class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        output = [] 
        for a in sorted(count.keys()):
            if count[a] != 0:
                if a == 0 and count[a] & 1:
                        return [] 
                output += [a] * (count[a] // 2 if a == 0 else count[a])
                count[2*a] -= count[a]
            count[a] = 0 
        if any(v !=0 for v in count.values()):
            return []
        return output 
       

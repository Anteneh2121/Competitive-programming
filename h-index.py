class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sort=sorted(citations)
        
        for cit in range(len(sort)):
            if sort[cit]>=len(sort)-cit:
                return len(sort)-cit
        return 0

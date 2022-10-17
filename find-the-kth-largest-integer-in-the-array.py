class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        #priority queue O(NlogK)
        pq = [] # min-heap 
        for x in nums: 
            heappush(pq, int(x))
            if len(pq) > k: heappop(pq)
        return str(pq[0])
        

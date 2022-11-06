from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        queue=deque([(nums[0],0)],maxlen=k)
        # max sliding windows
        for i in range(1,len(nums)):
            cur=queue[0][0]+nums[i]
            while queue and queue[-1][0]<=cur:
                queue.pop()
            queue.append((cur,i))
            while queue and queue[0][1]<=i-k:
                queue.popleft()
        return queue[-1][0]

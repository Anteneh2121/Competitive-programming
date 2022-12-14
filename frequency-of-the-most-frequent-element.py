class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt, ans, pre, hp = 1, 1, nums[0], [nums[0]]
        for num in nums[1:]:
            heapq.heappush(hp, num)
            k -= cnt * (num - pre)
            cnt += 1
            pre = num
            while k < 0:
                cur = heapq.heappop(hp)
                k += pre - cur
                cnt -= 1
            ans = max(ans, cnt)
        return ans

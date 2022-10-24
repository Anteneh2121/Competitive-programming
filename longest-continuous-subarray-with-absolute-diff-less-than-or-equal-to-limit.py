class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_len = 0
        max_stack, min_stack = deque(), deque()
        left, right = 0, 0
        while right < len(nums):
            while max_stack and nums[max_stack[-1]] < nums[right]:
                max_stack.pop()
            max_stack.append(right)
            while min_stack and nums[min_stack[-1]] > nums[right]:
                min_stack.pop()
            min_stack.append(right)
            
            while not (nums[max_stack[0]] - nums[min_stack[0]] <= limit):
                left += 1
                if left > max_stack[0]:
                    max_stack.popleft()
                if left > min_stack[0]:
                    min_stack.popleft()
                
            max_len = max(max_len, right - left + 1)
            right += 1
            
        return max_len

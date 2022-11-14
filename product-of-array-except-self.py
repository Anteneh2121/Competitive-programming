class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product except self
        # prefix = [1, 2,6, 24]
        # postfix = [24, 24, 12, 4]
        result = [1] * (len(nums))
        postfix = 1
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
            

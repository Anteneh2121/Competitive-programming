class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        n = len(nums)
        if n % 2 == 0:
            i, j = 1, len(nums) - 2
            while i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j -= 2
        else:
            i, j = 1, len(nums) - 1
            while i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j -= 2
        return nums

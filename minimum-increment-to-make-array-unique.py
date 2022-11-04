class Solution:
    def minIncrementForUnique(self, nums):
        nums.sort()
        i = 0
        num = 1
        count = 0
        while num < len(nums):
            if nums[num]==nums[i]:
                nums[num] += 1
                count += 1
            elif nums[num]<nums[i]:
                diff = (nums[i]-nums[num])+1
                nums[num] += diff
                count += diff
            num += 1
            i += 1

        return count

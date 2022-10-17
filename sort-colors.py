class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        redCount= nums.count(0)
        whiteCount= nums.count(1)
        blueCount= nums.count(2)
        for x in range(len(nums)):
            if redCount>0:
                nums[x]=0
                redCount-=1
            elif whiteCount>0:
                nums[x]=1
                whiteCount-=1
            elif blueCount>0:
                nums[x]=2
                blueCount-=1
        

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        cmp = lambda x, y: ((x+y) > (y+x)) - ((x+y) < (y+x))
        nums = sorted(nums, key=cmp_to_key(cmp))
        return str(int(''.join(nums[::-1])))
        

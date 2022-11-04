class Solution:
    def maxArea(self, height: List[int]) -> int:
        Left, Right = 0, len(height) - 1
        water = 0
        
        while Left < Right:
            water = max(water, (Right - Left) * min(height[Left], height[Right]))
            if height[Left] < height[Right]:
                Left += 1
            else:
                Right -= 1
        return water
        

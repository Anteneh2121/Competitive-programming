class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # T: O(n log n), S: O(n)
        res = len(speed)
        bottleneck_speed = -1
        for p, s in sorted(zip(position, speed))[::-1]:
            t = (target - p) / s
            if bottleneck_speed < t:
                bottleneck_speed = t
            else:
                res -= 1
        return res    

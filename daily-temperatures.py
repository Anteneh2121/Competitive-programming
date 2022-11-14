class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # deacrising stack
        stack = [] # index, temp, [i, t]
        n = len(temperatures)
        result = [0] * n
        for i in range(n):
            t = temperatures[i]
            while stack != [] and temperatures[stack[-1]] < t:
                stack_ind = stack.pop()
                result[stack_ind] = i - stack_ind
            stack.append(i)
        return result

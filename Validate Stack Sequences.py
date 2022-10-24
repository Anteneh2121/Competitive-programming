class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        n = len(pushed)
        
        count = 0
        for i in range(n):
            stack.append(pushed[i])
            while stack and stack[-1]==popped[count]:
                stack.pop()
                count+=1
            
        if stack:
            return False
        else:
            return True

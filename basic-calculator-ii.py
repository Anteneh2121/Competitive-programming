class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        operator = "+"
        operators = {"+", "-", "*", "/"}
        nums = set(str(x) for x in range(10))
        for index, char in enumerate(s):
            if char in nums:
                current_num = current_num * 10 + int(char)
            if char in operators or index == len(s) - 1:
                if operator == "+":
                    stack.append(current_num)
                elif operator == "-":
                    stack.append(-current_num)
                elif operator == "*":
                    stack[-1] = int(stack[-1] * current_num)
                else:
                    stack[-1] = int(stack[-1] / current_num)
                
                current_num = 0
                operator = char
        
        return sum(stack)

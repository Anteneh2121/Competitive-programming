# Reverse Substrings Between Each Pair of Parentheses
# You are given a string s that consists of lower case English letters and brackets.
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
# Your result should not contain any brackets.
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        reverse = []
        
        for i in range(len(s)):
            if s[i] == ')':  # pop the substring between nearest parentheses
                p = stack.pop()
                while p != '(':
                    reverse.append(p)
                    p = stack.pop()
                stack += reverse
                reverse = []
            else:
                stack.append(s[i])
        return ''.join(stack)
        

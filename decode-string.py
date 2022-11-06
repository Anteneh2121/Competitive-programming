class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        x, b = '', ''
        for letter in s:
            if letter.isdigit():
                b+=letter
            elif letter.isalpha():
                x+=letter
            elif letter=='[':
                stack.append((x, int(b)))
                x, b = '', ''
            elif letter==']':
                p, n = stack.pop()
                x = p+x*n
            
        return x

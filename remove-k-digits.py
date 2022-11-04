class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        digits = []
        for digit in num:
            while digits and digits[-1] > digit and k:
                digits.pop()
                k -= 1
            digits.append(digit)
        while k>0:
            digits.pop()
            k -= 1
        answer = "".join(digits).lstrip("0")
        if answer != "":
            return answer
        else:
            return "0"
            

# Evaluate Reverse Polish Notation
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another               expression.

# Note that division between two integers should truncate toward zero.

#It is guaranteed that the given RPN expression is always valid. That means the expression     would always evaluate to a result, and there will not be any division by zero operation.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def update(sign):
            t2,t1=stack.pop(),stack.pop()
            if sign=="+": return t1+t2
            if sign=="-": return t1-t2
            if sign=="*": return t1*t2
            if sign=="/": return int(t1/t2)
			
        stack=[]
        
        for t in tokens:
            if t.isdigit() or len(t)>1:
                stack.append(int(t))
            else:
                stack.append(update(t))
        return stack.pop()
        

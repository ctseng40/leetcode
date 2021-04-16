# Approach : Stack and No String Reversal
# Reference: https://leetcode.com/problems/basic-calculator/solution/
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        operand = 0
        res = 0 # for the on-going result
        sign = 1 # 1 means positive, -1 means negative
        
        for ch in s:
            if ch.isdigit():
                operand = (operand * 10) + int(ch) # int(ch)
            elif ch == '+':
                res += sign * operand
                sign = 1
                operand = 0
            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ch == ')':
                res += sign * operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0
        return res + sign * operand
                

# Approach 1: Pop and Push Digits & Check before Overflow
# Ref: https://leetcode.com/problems/reverse-integer/solution/
# In computing, an overflow error can occur when a calculation is run but the computer is unable to store the answer correctly. All computers have a predefined range of values they can represent or store. Overflow errors occur when the execution of a set of instructions return a value outside of this range.
# The term "unsigned" in computer programming indicates a variable that can hold only positive numbers. The term "signed" in computer code indicates that a variable can hold negative and positive values. The property can be applied to most of the numeric data types including int, char, short and long.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = 0
        rev = 0
        num = 0
        if x < 0:
            num = -x
        else:
            num = x
        
        while num != 0:
            pop = num % 10
            num /= 10
            if rev > ((2 ** 31) - 1)/10 or rev < -(2 ** 31)/10:
                return 0
            else:
                temp = rev * 10 + pop
                rev = temp
        if x < 0:
            rev = -rev
        
        return rev
        

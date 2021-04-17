#Approach: Dynamic programming
#Reference: https://leetcode.com/problems/longest-palindromic-substring/discuss/1158287/Python3

def checkPalindrome(string, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return
    while leftIdx >= 0 and rightIdx < len(string):
        if (string[leftIdx] != string[rightIdx]):
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx+1, rightIdx]
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestIdx = []
        size = 0
        for i in range(len(s)):
            oddIdx = checkPalindrome(s, i-1, i+1)
            evenIdx = checkPalindrome(s, i-1, i)
            if oddIdx and oddIdx[1] - oddIdx[0] > size:
                longestIdx = oddIdx
                size = oddIdx[1] - oddIdx[0]
            elif evenIdx and evenIdx[1] - evenIdx[0] > size:
                longestIdx = evenIdx
                size = evenIdx[1] - evenIdx[0]
        return s[longestIdx[0]:longestIdx[1]]

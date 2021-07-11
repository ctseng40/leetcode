# Approach 2: Two Pointer Approach
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        memo = {}
        i, j = 0, len(height)-1
        maxArea = [0]
        area = 0 
        def computeArea(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == j:
                return 0
            area = min(height[i], height[j]) * (j-i)
            memo[(i, j)] = area
            if area > maxArea[0]:
                maxArea.pop()
                maxArea.append(area)
            if  height[i] <= height[j] and i!=j:
                i += 1
                computeArea(i, j)
            if height[i] > height[j] and i!=j:
                j -= 1
                computeArea(i, j)
        computeArea(i, j)
        #print(memo)
        return maxArea[0]

# Brute Force (Time limit exceeded)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        memo = {}
        i, j = 0, 0
        maxArea = [0]
        area = 0 
        def computeArea(i, j):
            
            if (i, j) in memo:
                return memo[(i, j)]
            if i > len(height)-1 or j > len(height)-1:
                return False
            area = min(height[i], height[j]) * (j-i)
            memo[(i, j)] = area
            if area > maxArea[0]:
                maxArea.pop()
                maxArea.append(area)
            if  i < len(height)-1 and j < len(height)-1:
                j += 1
                computeArea(i, j)
            if i < len(height)-1 and j == len(height)-1:
                i += 1
                j = i+1
                computeArea(i, j)
        computeArea(i, j)
        #print(memo)
        return maxArea[0]

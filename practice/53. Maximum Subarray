import numpy as np
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_sum = np.sum(nums)
        
        for i in range(0, n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += nums[j]
                max_sum = max(max_sum, cur_sum)
                
        return max_sum

# Solution1
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
# Solution2
import numpy as np
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_so_far = nums[0]
        max_ending_here = nums[0]
        for i in range(1, n):
            max_ending_here = max (nums[i], max_ending_here+nums[i])
            max_so_far = max(max_ending_here, max_so_far)
                
        return max_so_far

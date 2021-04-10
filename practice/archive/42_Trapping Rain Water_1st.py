class Solution(object): # Dynamic programming
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        size = len(height)
        left_max = 0
        right_max = 0
        num_left = [0] * size
        num_right = [0] * size
        num = 0
        if not height:
            return num
        
        for i in range(size):
            if height[i] > left_max:
                left_max = height[i]
            
            if left_max > height[i]:
                num_left[i] = left_max - height[i]
            else:
                num_left[i] = 0
                
        for i in reversed(range(size)):
            if height[i] > right_max:
                right_max = height[i]
            
            if right_max > height[i]:
                num_right[i] = right_max - height[i]
            else:
                num_right[i] = 0
                
        l = len(num_left)
        for i in range(l):
            num += min(num_left[i],num_right[i])
        return num

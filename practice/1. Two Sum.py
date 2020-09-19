class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        required = {}
        required1 = {}
        for index, value in enumerate(nums): #2:0
            #print(index, value) 
            required1[value] = index
            print(required1)
            target1 = target - value #7
            if target1 in required:
                return[required[target1], index]
            else:
                required[value] = index

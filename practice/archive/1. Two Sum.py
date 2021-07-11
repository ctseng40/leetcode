# Solution 1
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
                
# Solution 2
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = dict()
        for i, elem in enumerate(nums):
            comp = target - elem
            if comp in values:
                return [values[comp], i]
            else:
                values[elem]=i
                
        return []

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)>=3:
            my_list = sub_nums = []
            for i, elem in enumerate(nums):
                sub_nums = nums[i+1:len(nums)]
                comp = 0 - elem
                
                for j, elem1 in enumerate(sub_nums):                 
                    comp1 = comp - elem1
                    a = []
                    a=sub_nums[j+1:len(sub_nums)]
                    if a.count(comp1)>=1:
                        my_list.append([elem,comp1,elem1])            
            for l in range(len(my_list)):
                my_list[l].sort()
            seen = []
            uniq = []
            for x in my_list:
                if x not in uniq:
                    uniq.append(x)
                    seen.append(x)
            return uniq
        else: return []
        

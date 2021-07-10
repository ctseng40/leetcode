class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # merge, sort, and find median
        # The overall run time complexity should be O(log (m+n))
        
        mergedList = nums1 + nums2
        
        def quicksort(arr):
            if len(arr) < 2:
                return arr
            else:
                pivot = arr[0]
                less = [i for i in arr[1:] if i <= pivot]
                greater = [i for i in arr[1:] if i > pivot]
            return quicksort(less) + [pivot] + quicksort(greater)
        

        def findMedian(arr):
            sortedmergedList =  quicksort(arr)
            if len(sortedmergedList)%2 != 0:
                index = (len(sortedmergedList)-1)/2
                median = sortedmergedList[index]
                return median
            else: 
                index1 = (len(sortedmergedList))/2
                index2 = index1 - 1
                median = 1.0* (sortedmergedList[index1] + sortedmergedList[index2])/2 # times 1.0 up front to get a float
                return median
            
        return findMedian(mergedList)

# Sorting then merging
# Time complexity : O(nlog n)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort by the first elements of all intervals, and then merge them 
        merge = []
        intervals.sort(key = lambda x:x[0])
        # print(intervals)
        
        for interval in intervals:
            if not merge or merge[-1][1] < interval[0]:
                merge.append(interval)
            else:
                merge[-1][1] = max(merge[-1][1], interval[1])
        
        return merge
        

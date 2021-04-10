# Approach: DFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# loop from the beginning, for each compare each entre with
class Result:
    def __init__(self):
        self.num = 0

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = Result()
        self.dfs(root, -float('inf'), result)
        return result.num
    
    def dfs(self, root, max_value, result):
        if not root:
            return
        if root.val >= max_value:
            result.num += 1
            max_value = root.val
        self.dfs(root.left, max_value, result)
        self.dfs(root.right, max_value, result)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(root, cur_sum):
            nonlocal max_sum
            if root is None:
                return 0
            
            left = max(0, dfs(root.left, cur_sum))
            right = max(0, dfs(root.right, cur_sum))
            cur_sum = root.val + left + right

            max_sum = max(max_sum, cur_sum)
            return root.val + max(left, right)

        dfs(root, float('-inf'))
        return max_sum 
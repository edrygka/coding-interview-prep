# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def something(self, node, targetSum, prev_sum):
        if not node:
            return False

        if not node.left and not node.right:
            if prev_sum + node.val == targetSum:
                return True
            else:
                return False

        prev_sum += node.val
        return self.something(node.left, targetSum, prev_sum) or self.something(node.right, targetSum, prev_sum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.something(root, targetSum, 0)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        stack = [(root, 0)]

        while stack:
            (curr, prev_sum) = stack.pop()
            if not curr.left and not curr.right and prev_sum + curr.val == targetSum:
                return True
            if curr.left:
                stack.append((curr.left, prev_sum + curr.val))
            if curr.right:
                stack.append((curr.right, prev_sum + curr.val))

        return False
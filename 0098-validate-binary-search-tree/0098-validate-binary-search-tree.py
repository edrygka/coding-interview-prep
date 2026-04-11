# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validateInRange(self, node, minV = -math.inf, maxV = math.inf):
        if not node:
            return True
        if not (minV < node.val) or not (node.val < maxV):
            return False
        return self.validateInRange(node.left, minV, node.val) and self.validateInRange(node.right, node.val, maxV)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validateInRange(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isIdentical(self, l1, l2):
        if not l1 and not l2:
            return True
        if not l1 or not l2:
            return False
        if l1.val != l2.val:
            return False
        return True and self.isIdentical(l1.left, l2.right) and self.isIdentical(l1.right, l2.left)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        return self.isIdentical(root.left, root.right)

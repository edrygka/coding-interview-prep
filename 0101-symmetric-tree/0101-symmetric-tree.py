# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True

        deque = collections.deque([(root.left, root.right)])

        while deque:
            (curr1, curr2) = deque.popleft()
            if not curr1 and not curr2:
                continue
            if not curr1 or not curr2:
                return False

            if curr1.val != curr2.val:
                return False
            
            deque.append((curr1.left, curr2.right))
            deque.append((curr1.right, curr2.left))
        return True
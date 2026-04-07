# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        deque = collections.deque([(root, 1)])
        while deque:
            (curr, min_depth) = deque.popleft()

            if curr.left:
                deque.append((curr.left, min_depth + 1))
            if curr.right:
                deque.append((curr.right, min_depth + 1))
            
            if not curr.left and not curr.right:
                return min_depth
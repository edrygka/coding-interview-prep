# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        deque = collections.deque([(root, 0)])
        
        while deque:
            (curr, prev_sum) = deque.popleft()
            if not curr:
                continue
            if not curr.left and not curr.right:
                if curr.val + prev_sum == targetSum:
                    return True

            prev_sum += curr.val
            deque.append((curr.left, prev_sum))
            deque.append((curr.right, prev_sum))

        return False
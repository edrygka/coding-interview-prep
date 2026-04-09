# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        deque = collections.deque([[root]])
        result = []
        while deque:
            level = deque.popleft()
            level_stack = []
            next_level = []
            for node in level:
                level_stack.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if len(level_stack) == 0:
                break
            result.append(level_stack)
            deque.append(next_level)
        return result

            
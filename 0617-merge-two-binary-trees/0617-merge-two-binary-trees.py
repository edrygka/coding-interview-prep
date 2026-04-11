# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        merged = TreeNode()
        queue = collections.deque([(root1, root2, merged)])
        while queue:
            (curr1, curr2, curr_merged) = queue.popleft()
            merged_val = 0
            if not curr1:
                merged_val += curr2.val
            elif not curr2:
                merged_val += curr1.val
            else:
                merged_val = curr1.val + curr2.val

            curr_merged.val = merged_val

            if (curr1 and curr1.left) or (curr2 and curr2.left):
                curr1_left = curr1.left if curr1 else None
                curr2_left = curr2.left if curr2 else None
                curr_merged.left = TreeNode()
                queue.append((curr1_left, curr2_left, curr_merged.left))
            if (curr1 and curr1.right) or (curr2 and curr2.right):
                curr1_right = curr1.right if curr1 else None
                curr2_right = curr2.right if curr2 else None
                curr_merged.right = TreeNode()
                queue.append((curr1_right, curr2_right, curr_merged.right))
        return merged
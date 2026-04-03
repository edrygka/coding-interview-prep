# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def is_valid(p, q):
            if not p and not q:
                return True
        
            if not p or not q:
                return False

            if p.val != q.val:
                return False
            return True

        deque = collections.deque([(p, q)])
        while deque:
            curr_p, curr_q = deque.popleft()
            if not is_valid(curr_p, curr_q):
                return False
            
            if curr_p:
                deque.append((curr_p.left, curr_q.left))
                deque.append((curr_p.right, curr_q.right))
        return True
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avgs = []
        deque = collections.deque([root])
        while deque:
            level_nodes_length = len(deque)
            sum = 0
            for i in range(level_nodes_length):
                curr = deque.popleft()
                if curr.left:
                    deque.append(curr.left)
                if curr.right:
                    deque.append(curr.right)
                sum += curr.val
            avgs.append(sum / level_nodes_length)
        return avgs

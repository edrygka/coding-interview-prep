# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first_node = ListNode(-1, head)
        prev = first_node
        curr = head
        i = 1
        
        while curr:
            if i >= n + 1:
                prev = prev.next
            curr = curr.next
            i += 1
        prev.next = prev.next.next
        return first_node.next
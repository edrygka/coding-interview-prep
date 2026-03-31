# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head
        prev = head
        while curr:
            if curr.val != prev.val:
                prev.next = curr
                prev = curr
            curr = curr.next
        prev.next = None
        return head
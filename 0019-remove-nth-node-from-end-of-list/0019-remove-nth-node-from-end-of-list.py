# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = ListNode(-1, head)
        curr = new_head
        prev = new_head
        for i in range(n):
            curr = curr.next

        while curr.next:
            prev = prev.next
            curr = curr.next

        prev.next = prev.next.next
        return new_head.next
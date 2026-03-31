# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode(-1)
        curr_merged = merged
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val > curr2.val:
                curr_merged.next = curr2
                curr2 = curr2.next
            else:
                curr_merged.next = curr1
                curr1 = curr1.next
            curr_merged = curr_merged.next

        curr_merged.next = curr1 or curr2
        return merged.next
            
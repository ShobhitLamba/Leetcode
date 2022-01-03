# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        head = sentinel
        l1_head, l2_head = list1, list2

        while l1_head and l2_head:
            if l1_head.val > l2_head.val:
                sentinel.next = l2_head
                l2_head = l2_head.next
            else:
                sentinel.next = l1_head
                l1_head = l1_head.next

            sentinel = sentinel.next

        sentinel.next = l1_head if l1_head else l2_head

        return head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        predecessor, current = head, head.next

        while current is not None:
            if current.val == predecessor.val:
                predecessor.next = current.next
                current = current.next

            else:
                current = current.next
                predecessor = predecessor.next

        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        end_first = self.first_half_end(head)
        second_start = self.reverse_list(end_first.next)

        first, second = head, second_start

        while second:
            if first.val != second.val:
                return False
            first, second = first.next, second.next

        end_first.next = self.reverse_list(second_start
        
        return True

    def first_half_end(self, head):
        fast, slow = head, head
        while fast.next is not None and fast.next.next is not None:
            fast, slow = fast.next.next, slow.next

        return slow

    def reverse_list(self, head):
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        tortoise, rabbit = head, head.next

        while tortoise != rabbit:
            if rabbit is None or rabbit.next is None:
                return False

            tortoise = tortoise.next
            rabbit = rabbit.next.next

        return True    

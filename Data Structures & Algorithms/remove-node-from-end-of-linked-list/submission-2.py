# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # offset pointer algorithm
        dummy = ListNode(0)
        prev = dummy
        l , r = head, head

        dummy.next = l

        for i in range(n):
            r = r.next
        
        while r:
            r = r.next
            l = l.next
            prev = prev.next
        
        prev.next = l.next

        return dummy.next
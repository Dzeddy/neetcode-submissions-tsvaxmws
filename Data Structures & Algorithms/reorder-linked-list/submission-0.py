# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # obviously doing it through brute force is trivial. we can just push it to a deque and popleft popright
        deq = deque([])

        dummy = ListNode(0)
        dummy.next = head

        while head:
            deq.append(head)
            head = head.next
        
        prev = dummy

        while deq:
            l = deq.popleft()
            print(l.val)
            r = deq.pop() if deq else None
            prev.next = l
            l.next = r
            prev = r

        if prev:
            prev.next = None

        return None
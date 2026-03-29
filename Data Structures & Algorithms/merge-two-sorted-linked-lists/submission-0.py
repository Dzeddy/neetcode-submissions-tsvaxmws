# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = head = ListNode(0)
        while list1 and list2:
            l = list1.val
            r = list2.val
            if l < r:
                res.next = list1
                res = res.next
                list1 = list1.next
            else:
                res.next = list2
                res = res.next
                list2 = list2.next
        fin = list1 if list1 else list2
        res.next = fin
        return head.next
                

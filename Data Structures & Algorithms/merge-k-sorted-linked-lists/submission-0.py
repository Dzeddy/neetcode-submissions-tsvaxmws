import itertools
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        counter = itertools.count()
        if not lists:
            return None
        
        heap = []        

        res = []

        for i in range(len(lists)):
            curr = lists[i]
            if curr:
                tup = (curr.val, next(counter), curr)
                heapq.heappush(heap, tup)
        
        heapq.heapify(heap)

        prev = None

        if not heap:
            return None

        head = heap[0][2]

        while heap:
            curr_val, _, curr = heapq.heappop(heap)
            if curr.next:
                tup = (curr.next.val, next(counter), curr.next)
                heapq.heappush(heap, tup)
            if prev:
                prev.next = curr
            prev = curr
        
        return head
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mapp = {}

        mapp[head] = Node(head.val)

        ptr = head

        while head:
            print(head.val)
            print(mapp)
            print()
            if head.random and head.random in mapp:
                mapp[head].random = mapp[head.random]
            elif head.random:
                mapp[head].random = Node(head.random.val)
                mapp[head.random] = mapp[head].random
            
            if head.next and head.next in mapp:
                mapp[head].next = mapp[head.next]
            elif head.next:
                mapp[head].next = Node(head.next.val)
                mapp[head.next] = mapp[head].next
            
            head = head.next

        return mapp[ptr]
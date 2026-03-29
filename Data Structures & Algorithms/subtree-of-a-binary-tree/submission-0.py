# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # traverse tree for nodes with the same value as subroot
        # for each node, check if it's a copy of subroot
        # if it's not true for the entire set, summarize that there is no such thing

        # o(root * subroot)\

        stack = []

        curr = root

        res = []

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.val == subRoot.val:
                res.append(curr)
            curr = curr.right
        
        print([i.val for i in res])

        # now we iterate through the res and check each for if it's a copy
        
        found = False

        while res:
            curr = res.pop()

            temp = subRoot

            stack = [(curr, temp)]
            
            err = False

            while stack:
                p_c, q_c = stack.pop()

                if not p_c and not q_c:
                    continue

                if p_c and not q_c:
                    err = True
                    break
                
                if q_c and not p_c:
                    err = True
                    break
                
                if p_c.val != q_c.val:
                    err = True
                    break
                
                stack.append([p_c.left, q_c.left])
                stack.append([p_c.right, q_c.right])
            
            if not err:
                found = True
                break
        
        return found
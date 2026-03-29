from collections import deque
def spin_lock(arr, i):
    carr = list(arr)
    left = (arr[i] - 1) % 10
    right = (arr[i] + 1) % 10
    larr = carr.copy()
    rarr = carr.copy()
    larr[i] = left
    rarr[i] = right
    return [tuple(larr), tuple(rarr)]

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # first define the initial state
        # then consider the states surrounding the initial state
        # store deadends in our initial state. 
        # 10**4 possible combinations, 8 possible moves per one, so ~4 * 10**5 edges. 
        # 4-d BFS is possible, as it would be v + e which is within the bounds of most compilers

        # we can simulate a lock turn with n + 1 % 10 and n - 1 % 10. this will give us 0 -> -1 % 10 = 9 and 
        # 10 -> 11 % 10 = 1. using this, we can store the adjacent states of every single string
        # after this, we can prune the ones that exist in deadends, and mark the current strings as visited

        target_nums = tuple([int(i) for i in target])

        dead_set = set([tuple([int(k) for k in i]) for i in deadends])

        queue = deque([target_nums])
        mapp = {target_nums : 0}

        while queue:
            curr = queue.popleft()
            
            if curr == tuple([0,0,0,0]):
                break

            for i in range(len(curr)):
                turns = spin_lock(curr, i)
                left = turns[0]
                right = turns[1]
                if left not in mapp and left not in dead_set:
                    mapp[left] = mapp[curr] + 1
                    queue.append(left)
                if right not in mapp and right not in dead_set:
                    mapp[right] = mapp[curr] + 1
                    queue.append(right)
                
        return mapp[tuple([0,0,0,0])] if tuple([0,0,0,0]) in mapp else -1
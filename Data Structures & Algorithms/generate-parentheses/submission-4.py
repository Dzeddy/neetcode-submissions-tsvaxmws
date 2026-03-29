class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we are generating permutations of ( and ) where the case must be that for every open there must be a close
        kek = "()"

        res = []

        path = []

        taken = [n for _ in range(len(kek))] 

        def dfs():
            if taken[1] - taken[0] < 0:
                return

            if len(path) == n * 2:
                # have to check if it's valid
                # problem: this option is n!. how can we avoid duplicates?
                # how about: instead of generate -> validate, we try to track the number of open bracket parentheses
                # that way, we can only add a close bracket if there is an open bracket before
                # we still need to further prune the tree. how can we do this?
                # we are already returning situations where there are more open than there are closed. 
                s = "".join(path)
                # if validate_str(s):
                res.append(s)
            
            for i in range(len(kek)):
                if not taken[i]:
                    continue
                taken[i] -= 1

                path.append(kek[i])

                dfs()

                path.pop()

                taken[i] += 1
        
        dfs()

        return res
                
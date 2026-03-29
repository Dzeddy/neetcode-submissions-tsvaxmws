class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # obvious solution: create every single combination of substrings.
        # for every string, there are n! ways to partition it
        # we then have 2^n * n time to identify every partition and validate every substring
        # this is obviously not desirable
        # instead, we can only explore a subset further if the previous strings are palindromes
        res = []

        path = []

        def dfs(i):
            # first change: instead of just adding every single subset, we only add the ones which have 
            # reached the end of the string
            if i == len(s):
                res.append(path.copy())
            
            # second change: we choose to append the slice instead of our current string. we also have to 
            # go further (reach the end of the array + 1) to terminate. we also skip j = i case
            for j in range(i + 1, len(s) + 1):
                # take
                # path.append(s[i:j])
                # we only want to dfs if our previous substrings were all palindromes. arguably, we should 
                # kill this situation quicker (at the start b4 iterations)
                substr = s[i:j]

                if substr[::-1] != substr:
                    continue
                path.append(substr)
                dfs(j)
                # skip
                path.pop()

        dfs(0)

        return res
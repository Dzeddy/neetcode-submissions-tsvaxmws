class Solution:
    # optimization in the future: instead of comparing arrays, check only the index of the added character and the total missing count, which allows us to only perform one check instead of iterating over the whole array each time
    def minWindow(self, s: str, t: str) -> str:
        # iterate over s
        # correct output always unique
        # obvious solution: iterate over all substrings of s, and return the shortest substring which contains 
        # the same number of characters as t. this is o(2^s * s) and not worth it

        # we can use a sliding window, and skip every single starting index that isn't contained in t.
        # after we choose a starting index, we can iterate down the rest of s, and check if we've contained the result of t
        # if we reach the end without finding everything in t, we can say that we've already found our min string
        # and return that 
        def char_to_int(c):
            if 'a' <= c and c <= 'z':
                return ord(c) - ord('a')
            elif 'A' <= c and c <= 'Z':
                return ord(c) - ord('A') + 26

        def cmp_arr(s_arr, t_arr):
            for i in range(52):
                if t_arr[i] - s_arr[i] > 0:
                    # there are letters in t that aren't in our current subset
                    return False
            return True
        l = 0 
        r = 0

        tsett = set(t)

        tarr = [0 for _ in range(52)]

        for i in range(len(t)):
            tarr[char_to_int(t[i])] += 1

        # we can initialize a new sarr every single time

        maximillian = 10**6

        idx = (0,0)

        flag = False

        # for i in range(len(s)):
        #     if flag:
        #         break
        #     if s[i] not in tsett:
        #         continue
        #     sarr = [0 for _ in range(52)]
        #     for j in range(i, len(s)):
        #         sarr[char_to_int(s[j])] += 1
        #         if cmp_arr(sarr, tarr):
        #             if j - i + 1 < maximillian:
        #                 maximillian = j - i + 1
        #                 idx = (i, j + 1)
        #                 break
        #         elif j == len(s) - 1:
        #             flag = True
        
        # logic above works but TLEs. What if we iterate down s, and then jump if we find a substring that works

        l = 0
        r = 0

        sarr = [0 for _ in range(52)]

        while r < len(s):
            if s[l] not in tsett:
                sarr[char_to_int(s[l])] -= 1
                l += 1
            
            sarr[char_to_int(s[r])] += 1 # here, we added 1 to r, and incremented it, then used it to calculate
            # however, what about the case where the answer is at the start? how can we make our code more robust
            r += 1
            
            if cmp_arr(sarr, tarr):
                if r - l < maximillian:
                    maximillian = r - l
                    idx = (l, r)

                flag = False

                while l < r and cmp_arr(sarr, tarr):
                    # bring the window in, subtracting the results
                    # we should only do this until we've subtracted a singular important character. 
                    # however, we also want to prune the window so we don't include extraneous characters
                    if r - l < maximillian:
                        maximillian = r - l
                        idx = (l, r)
                    sarr[char_to_int(s[l])] -= 1
                    l += 1

        return s[idx[0]:idx[1]]
class Solution:
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

        for i in range(len(s)):
            if s[i] not in tsett:
                continue
            sarr = [0 for _ in range(52)]
            for j in range(i, len(s)):
                sarr[char_to_int(s[j])] += 1
                if cmp_arr(sarr, tarr):
                    if j - i + 1 < maximillian:
                        maximillian = j - i + 1
                        idx = (i, j + 1)
        
        return s[idx[0]:idx[1]]
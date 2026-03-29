class Solution:
    def numDecodings(self, s: str) -> int:
        # we have 1012 
        # this can either be 10 1 2 or 10 12
        # at each point, we have to consider the case that we take 2 digits, or the case that we take 1
        # if we can treat the number as a 2 digit number, we should sum the number of ways we can decode the previous subsequence
        # as well as the ways that we can decode it if we treat it as a one digit number

        def dp(i):
            if i >= len(s):
                return 1
            
            if s[i] == '0':
                return 0
                
            if i == len(s) - 1:
                return 1
            
            numways = dp(i + 1)

            if int(s[i:i + 2]) <= 26:
                numways += dp(i + 2) 
            
            return numways
        
        return dp(0)
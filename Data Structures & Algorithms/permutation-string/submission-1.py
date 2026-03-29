class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # iterate down s2, keep track of the letters. if at any point you have the 
        # same letters as in s1, return True
        # else return False

        def char_to_int(c):
            return ord(c) - ord('a')

        if len(s2) < len(s1):
            return False
        elif s2 == s1:
            return True

        l = 0

        s1arr = [0 for _ in range(26)]
        s2arr = [0 for _ in range(26)]

        for i in range(len(s1)):
            s1arr[char_to_int(s1[i])] += 1
            s2arr[char_to_int(s2[i])] += 1
        
        if s2arr == s1arr:
            return True

        prev = 0
        
        for i in range(len(s1), len(s2)):
            s2arr[char_to_int(s2[prev])] -= 1
            s2arr[char_to_int(s2[i])] += 1
            if s2arr == s1arr:
                return True
            prev += 1

        return False
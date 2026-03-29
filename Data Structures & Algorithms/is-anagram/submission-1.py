class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_map[s[i]] += 1
            s_map[t[i]] -= 1

        return sorted(s_map.values())[0] == 0
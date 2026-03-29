def to_freqmap(s):
    dick = defaultdict(int)
    for i in s:
        dick[i] += 1
    return dick
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return to_freqmap(s) == to_freqmap(t)
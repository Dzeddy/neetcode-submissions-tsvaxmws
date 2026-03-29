def to_freqmap(s):
    dick = [0] * 26
    for i in s:
        dick[ord(i) - ord('a') + 1] += 1
    return str(dick)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)
        for i in strs:
            mapp[to_freqmap(i)].append(i)
        return list(mapp.values())
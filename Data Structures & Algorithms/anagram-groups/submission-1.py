class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = 0
        dick = defaultdict(list)
        arr = [[]]
        for i in strs:
            lol = str(sorted(i))
            dick[lol].append(i)
        return dick.values()
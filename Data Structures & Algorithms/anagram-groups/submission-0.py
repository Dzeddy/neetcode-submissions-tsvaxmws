class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = 0
        dick = {}
        arr = [[]]
        for i in strs:
            lol = str(sorted(i))
            if lol in dick:
                arr[dick[lol]].append(i)
            else:
                dick[lol] = counter
                if len(arr) == counter:
                    arr.append([])
                arr[counter].append(i)
                counter += 1
        return arr
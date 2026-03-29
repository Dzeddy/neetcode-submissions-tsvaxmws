class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'

        kek = list(set("".join(words)))

        indegree = defaultdict(int)

        adjlist = defaultdict(set)

        for i in range(len(words) - 1):
            prev_word = words[i]
            next_word = words[i + 1]

            # iterate down the words and find the first letter that isn't the same
            for k in range(len(words[i])):
                if k > len(words[i + 1]) - 1:
                    return ""
                l = words[i][k]
                r = words[i + 1][k]

                if l != r:
                    if r not in adjlist[l]:
                        adjlist[l].add(r)
                        indegree[r] += 1
                    break
                    
        print(indegree)
        print(adjlist)

        # standard top sort from here on
        queue = deque([])

        for i in kek:
            if indegree[i] == 0:
                queue.append(i)
        
        res = []

        while queue:
            curr = queue.popleft()
            res.append(curr)
            for i in adjlist[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        print(res)

        return "".join(res) if len(res) == len(kek) else ""
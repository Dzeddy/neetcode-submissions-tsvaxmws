import string

def wordmutations(s):
    arr = list(s)

    letters = list(string.ascii_lowercase)

    res = []

    for i in range(len(arr)):
        for j in letters:
            if arr[i] != j:
                curr = arr.copy()
                curr[i] = j
                res.append("".join(str(i) for i in curr))
    return res


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # obviously if endword is not in wordlist, we can't use it
        # we need to decompose this problem into two problems: an adjacencylist initialization problem & a 
        # bfs problem, where we start at beginword

        # how can we create an adjacencylist from our graph? 
        # edges are detected from strings that differ by at most 1
        # we can iterate through 
        # can iterate through wordlist and initiate adjlist through brute force
        # however that runs into significant time complexity issues, as we are dancing around 2.5 * 10^7 max iterations for that alone.

        # another option: initiate a set with wordlist, and bfs using the adjacent words to beginword

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([beginWord])

        mapp = {beginWord : 1}

        while queue:
            curr = queue.popleft()
            neighbors = wordmutations(curr)

            for j in neighbors:
                if j in wordSet and j not in mapp:
                    mapp[j] = mapp[curr] + 1
                    queue.append(j)
        print(mapp)
        return mapp[endWord] if endWord in mapp else 0
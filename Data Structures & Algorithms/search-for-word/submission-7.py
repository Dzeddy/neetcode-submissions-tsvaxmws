class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        mapp = {}
        found = False
        path = set()
        def dfs(i, j, idx):
            nonlocal found
            if found:
                return True

            if (i, j) in path:
                return False

            if idx >= len(word):
                found = True
                return True

            if i < 0 or i > len(board) - 1:
                return False
            if j < 0 or j > len(board[0]) - 1:
                return False
            
            print(i, j)
            print(board[i][j])

            if word[idx] != board[i][j]:
                return False

            for k in dirs:
                path.add((i, j))
                if dfs(i + k[0], j + k[1], idx + 1):
                    found = True
                path.remove((i, j))
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dfs(i,j,0)

        return found
                        
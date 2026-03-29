class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        # track current visited
        # add to visited if X and processed or converted to X or if currently on iterating
        # track if hits edge. if finishes bfs and doesn't hit edge, color in. else, don't

        visited = set()

        res = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                surrounded = False
                curr = (i, j)
                q = deque([curr])

                if curr in visited:
                    continue

                if board[i][j] != 'O':
                    continue

                fill = set()

                while q:
                    i_curr, j_curr = q.popleft()

                    if (i_curr, j_curr) in visited:
                        continue

                    visited.add((i_curr, j_curr))

                    if i_curr < 0 or i_curr >= len(board) or j_curr < 0 or j_curr >= len(board[0]):
                        continue

                    if board[i_curr][j_curr] == 'X':
                        continue
                    else:
                        fill.add((i_curr, j_curr))

                    if (i_curr == 0 or i_curr == len(board) - 1 or j_curr == 0 or j_curr == len(board[0]) - 1) and board[i_curr][j_curr] == 'O':
                        surrounded = True

                    for k in range(4):
                        i_next, j_next = i_curr + dx[k], j_curr + dy[k]

                        q.append((i_next, j_next))

                if fill and not surrounded:
                    for x, y in fill:
                        board[x][y] = 'X'
                    

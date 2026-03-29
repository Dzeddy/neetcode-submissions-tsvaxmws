class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check horizontal
        for i in board:
            sett = set()
            for j in i:
                if j == ".":
                    continue
                if j in sett:
                    return False
                sett.add(j)
        
        for j in range(len(board[0])):
            sett = set()
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in sett:
                    return False
                sett.add(board[i][j])
        
        #check 3x3 square
        for square_x in range(3):
            for square_y in range(3):
                # 0 1 2, 0 1 2
                sett = set()
                for i in range(3):
                    for j in range(3):
                        curr = board[3*square_x + i][3*square_y + j]
                        if curr == ".":
                            continue
                        if curr in sett:
                            return False
                        sett.add(curr)
        
        return True
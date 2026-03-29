class Solution:
    def check_row(self, arr):
        sett = set()
        for i in arr:
            if i != ".":
                if i in sett:
                    return False
                else:
                    sett.add(i)
        return True
    
    def check_column(self, arr, col):
        sett = set()
        for i in range(0,9):
            if arr[i][col] != ".":
                if arr[i][col] in sett:
                    return False
                else:
                    sett.add(arr[i][col])
        return True
    
    def check_square(self, arr, iloc, jloc):
        sett = set()
        row_start = iloc * 3
        col_start = jloc * 3

        for i in range(3):
            for j in range(3):
                val = arr[row_start + i][col_start + j]
                if val != ".":
                    if val in sett:
                        return False
                    else:
                        sett.add(val)
        return True

        

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.check_row(board[i]) or not self.check_column(board, i):
                return False
        
        for i in range(3):
            for j in range(3):
                if not self.check_square(board, i, j):
                    return False

        return True

        
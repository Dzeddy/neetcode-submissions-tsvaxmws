class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # naive solution: iterate over board. select spot. then, iterate over board, and test spots until
        # we find a second spot that is not under attack from the first
        # iterate for third, and so on.
        # after we finish the entire board, if we were not able to place four queens, pop back to the original queen placement
        # and iterate for second placement. do this until we have checked every permutation of spots on the chess board.
        # this will require n^2 initial iterations (obvious) * n^2 2nd iterations for the 2nd queen * ~~~ = n^8 iterations

        # ways we can speed this up:
        # we must first prune rows and columns to check states. for example, we cannot place a queen on row 2 if there is already
        # a queen on row 2. similarly, we can not place on column 2 if there is a queen on column 2.
        # what this means for n queens is that each queen must have a unique row and a unique column
        # we also prune corner tiles for obvious reasons, as they would eliminate 2 queens from being able to be placed.
        # in addition, if we find a board, we are able to mirror the board on the x and y axis to speed up our solution. as such, we need only test
        # our first queen in the first quadrant of the board.

        def does_intersect(queens, space):
            # queens should contain just the current position of queens
            # linear time check
            for i in queens:
                if space[0] == i[0]:
                    return True
                if space[1] == i[1]:
                    return True
                if abs(space[0] - i[0]) == abs(space[1] - i[1]):
                    return True
            return False

        res = []

        path = []

        visited = set()

        def dfs(i, j):
            if len(path) == n:
                kek = path.copy()
                kek.sort()
                res.append(tuple(kek))
                return

            if i < 0 or i >= n:
                return
            if j < 0 or j >= n:
                return

            i_next = i + 1
            j_next = j

            if i_next >= n:
                i_next = i_next % n
                j_next += 1

            if i_next < 0 or i_next >= n:
                return
            if j_next < 0 or j_next >= n:
                return

            dfs(i_next, j_next)

            if not does_intersect(path, [i_next, j_next]):
                path.append((i_next, j_next))
                dfs(i_next, j_next)
                path.pop()
            # weakness: we have currently developed a greedy algorithm that only takes.

        for i in range(n):
            for j in range(n):
                # place first queen @ i, j
                path.append((i, j))
                dfs(i, j)
                path.pop()

        print(len(res))

        fin = []

        for i in res:
            temp = []
            for k in i:
                row = "." * (k[1]) + "Q" + "." * (n - k[1] - 1)
                temp.append(row)
            fin.append(temp)


        return fin

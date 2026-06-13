class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []
        cols = set()
        d1 = set()
        d2 = set()
        def helper(r):
            if r == n:
                copy = ["".join(row)for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or r + c in d1 or r - c in d2:
                    continue
                cols.add(c)
                d1.add(r+c)
                d2.add(r-c)
                board[r][c] = "Q"
                helper(r+1)
                cols.remove(c)
                d1.remove(r+c)
                d2.remove(r-c)
                board[r][c] = "."
        helper(0)
        return res
                

        
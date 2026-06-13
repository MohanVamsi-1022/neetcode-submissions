class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        cols = set()
        d1 = set()
        d2 = set()
        def helper(r):
            if r == n:
                self.res += 1
                return 
            for c in range(n):
                if c in cols or r + c in d1 or r - c in d2:
                    continue
                cols.add(c)
                d1.add(r+c)
                d2.add(r-c)
                helper(r+1)
                cols.remove(c)
                d1.remove(r+c)
                d2.remove(r-c)
        helper(0)
        return self.res
                
        
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True
        for i in range(n):
            for j in range(i):
                if s[i] == s[j] and (i - j <= 2 or is_pal[j + 1][i - 1]):
                    is_pal[j][i] = True
        def helper(i,path):
            if i == len(s):
                res.append(path[:])
                return
            for j in range(i,len(s)):
                if is_pal[i][j]:
                    path.append(s[i:j+1])
                    helper(j+1,path)
                    path.pop()
        helper(0,[])
        return res
        
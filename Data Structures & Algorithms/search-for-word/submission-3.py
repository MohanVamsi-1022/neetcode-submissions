class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = [[False] * (m) for _ in range(n)]
        def dfs(r,c,i):

            if i == len(word):
                return True
            if r < 0 or r >= n or c < 0 or c >= m or word[i] != board[r][c] or visited[r][c]:
                return False
            visited[r][c] = True
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            visited[r][c] = False
            return res    
            
        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True
        return False
                

        
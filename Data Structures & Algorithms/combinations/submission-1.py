class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(idx,path):
            if len(path) == k:
                res.append(path[:])
                return 
            for j in range(idx,n+1):
                path.append(j)
                helper(j+1,path)
                path.pop()
        helper(1,[])
        return res
        
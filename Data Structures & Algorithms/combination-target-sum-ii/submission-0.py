class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        def helper(i,total):
            if total == target:
                res.append(path[:])
                return 
            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if total + candidates[j] > target:
                    return 
                path.append(candidates[j])
                helper(j+1,total + candidates[j])
                path.pop()
            
        helper(0,0)
        
        return res
                
        
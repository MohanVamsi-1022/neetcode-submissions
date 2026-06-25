class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def helper(idx,curr):
            if idx == len(nums):
                return 1 if curr == target else 0
            key = (idx,curr)
            if key in memo:
                return memo[key]
            add = helper(idx+1,curr+nums[idx])
            sub = helper(idx+1,curr-nums[idx])
            res = add + sub
            memo[key] = res
            return res
        return helper(0,0)
            

        
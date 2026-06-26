class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        def helper(i,j):
            if i > j:
                return 0
            key = (i,j)
            if key in memo:
                return memo[key]
            ans = 0
            for k in range(i,j+1):
                curr = nums[k] * nums[i-1] * nums[j+1] + helper(i,k-1) + helper(k+1,j)
                ans = max(ans,curr)
            memo[key] = ans
            return ans
        return helper(1,len(nums)-2)


        
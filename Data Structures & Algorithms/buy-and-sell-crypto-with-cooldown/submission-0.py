class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def helper(idx,hold):
            if idx >= len(prices):
                return 0
            key = (idx,hold)
            if key in memo:
                return memo[key]
            ans = helper(idx+1,hold) # skip
            if hold:
                ans = max(ans, prices[idx] + helper(idx+2,False))
            else:
                ans = max(ans, -prices[idx] + helper(idx+1,True))
            memo[key] = ans
            return ans
        return helper(0,False)



        
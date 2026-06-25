class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def helper(start,total):
            if total == n:
                return 1
            if total > n:
                return float("-inf")
            key = (start,total)
            if key in memo:
                return memo[key]
            res = 1
            for num in range(start,n):
                res = max(res, num * helper(num,total + num))
            memo[key] = res
            return res
        return helper(1,0)
        

        
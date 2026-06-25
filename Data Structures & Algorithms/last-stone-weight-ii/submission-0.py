class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        n = len(stones)
        dp = [[0] * (target+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for t in range(target+1):
                skip = dp[i-1][t]
                choose = 0
                if stones[i-1] <= t:
                    choose = stones[i-1] + dp[i-1][t-stones[i-1]]
                dp[i][t] = max(skip,choose)
        return total - 2 * dp[n][target]
        
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        memo  = {}
        def helper(i,prev):
            if i == len(intervals):
                return 0
            key = (i,prev)
            if key in memo:
                return memo[key]
            skip = helper(i+1,prev)
            choose = 0
            if prev == -1 or intervals[i][0] >= intervals[prev][1]:
                choose = 1 + helper(i+1,i)
            memo[key] = max(skip,choose)
            return memo[key]
        maxx = helper(0,-1)
        return len(intervals) - maxx
     



        
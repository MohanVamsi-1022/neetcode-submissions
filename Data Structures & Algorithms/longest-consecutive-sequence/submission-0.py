class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        max_len = float("-inf")
        sett = set(nums)
        for num in nums:
            streak,curr = 0,num
            while curr in sett:
                streak += 1
                curr += 1
                max_len = max(max_len,streak)
        return max_len
            
            


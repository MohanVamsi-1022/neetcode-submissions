class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        ans = 0
        for num in range(n):
            ans ^= num
        for num in nums:
            ans ^= num
        return ans
        
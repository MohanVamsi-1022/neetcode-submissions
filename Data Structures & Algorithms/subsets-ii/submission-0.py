class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        nums.sort()
        def helper(i):
            if i == len(nums):
                res.append(path[:])
                return 
            path.append(nums[i])
            helper(i+1)
            path.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            helper(i+1)
        helper(0)
        return res

        
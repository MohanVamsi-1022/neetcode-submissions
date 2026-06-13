class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        subsets = [0] * k
        nums.sort(reverse = True)
        def helper(i):
            if i == len(nums):
                return True
            for s in range(k):
                if subsets[s] + nums[i] <= target:
                    subsets[s] += nums[i]
                    if helper(i+1):
                        return True
                    subsets[s] -= nums[i]
                if subsets[s] == 0:
                    break
            return False
        return helper(0)


        
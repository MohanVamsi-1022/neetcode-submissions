class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def helper(i):
            if i == len(nums):
                res.append(nums[:])
                return 
            sett = set()
            for j in range(i,len(nums)):
                if nums[j] in sett:
                    continue
                sett.add(nums[j])
                nums[i], nums[j] =  nums[j] , nums[i]
                helper(i+1)
                nums[i], nums[j] =  nums[j] , nums[i]
        helper(0)
        return res

        
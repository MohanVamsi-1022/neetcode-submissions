class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [0] * n
        suffix_product = [0] * n
        res = [0] * n
        prefix_product[0] = suffix_product[n-1] = 1
        for i in range(1,n):
            prefix_product[i] = nums[i-1] * prefix_product[i-1]
        for i in range(n-2,-1,-1):
            suffix_product[i] = nums[i+1] * suffix_product[i+1]
        for i in range(n):
            res[i] = prefix_product[i] * suffix_product[i]
        return res
        
        
        


            
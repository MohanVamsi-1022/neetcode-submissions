class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        res = nums[:]
        for num in nums:
            res.append(num)
        return res


        

        
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currsum = 0
        prefixsum = {0 : 1}
        for n in nums:
            currsum += n
            diff = currsum - k
            res += prefixsum.get(diff,0)
            prefixsum[currsum] = 1 + prefixsum.get(currsum,0)
        return res

        


        





        
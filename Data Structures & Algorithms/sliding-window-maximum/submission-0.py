class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        res = []
        l = 0

        for r in range(len(nums)):
            dict1[nums[r]] = 1 + dict1.get(nums[r], 0)

           
            if r - l + 1 == k:
                res.append(max(dict1.keys()))

               
                dict1[nums[l]] -= 1
                if dict1[nums[l]] == 0:
                    del dict1[nums[l]]
                l += 1

        return res

            
            

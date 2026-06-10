class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def is_possible(val):
            curr = 0
            count = 0
            for num in nums:
                curr += num
                if curr > val:
                    count += 1
                    if count + 1 > k:
                        return False
                    curr = num
            return True
        l, r = max(nums), sum(nums)
        res = l
        while l <= r:
            mid = (l + r)//2
            if is_possible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

        
            

        



        


        
        

        
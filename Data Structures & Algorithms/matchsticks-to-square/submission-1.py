class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        length = total // 4
        sides = [0] * 4
        nums = matchsticks[:]
        nums.sort(reverse = True)
        n = len(nums)
        def helper(i):
            if i == n:
                return sides[0] == sides[1] == sides[2] == sides[3]
            for side in range(4):
                if nums[i] + sides[side] <= length:
                    sides[side] += nums[i]
                    if helper(i+1):
                        return True
                    sides[side] -= nums[i]
                if sides[side] == 0:
                    break
            return False
        return helper(0)    
                    


        
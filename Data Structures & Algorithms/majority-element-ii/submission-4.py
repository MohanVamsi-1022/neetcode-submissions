class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []
        for keys in c:
            if c[keys] > len(nums)//3:
                res.append(keys)
        return res
        

        
            
                
        
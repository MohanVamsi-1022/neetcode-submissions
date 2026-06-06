class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        for i in range(len(nums)):
            dict1[nums[i]] = 1 + dict1.get(nums[i],0)
        sorted_dict = dict(sorted(dict1.items(),key = lambda item:item[1]))
        sorted_list = list(sorted_dict.keys())
        return sorted_list[-1]

        
        
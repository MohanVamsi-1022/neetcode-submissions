class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for i in range(len(strs)):
            new_ch = "". join(sorted(strs[i]))
            if new_ch in dict1:
                dict1[new_ch].append(strs[i])
            else:
                dict1[new_ch] = [strs[i]]
        return list(dict1.values())

        
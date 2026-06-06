class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for i in range(len(s1)):
            dict1[s1[i]] += 1
            dict2[s2[i]] += 1 
        i = 0
        for j in range(len(s1),len(s2)):
            if dict1 == dict2:
                return True
            dict2[s2[j]] += 1
            dict2[s2[i]] -= 1
            if dict2[s2[i]] == 0:
                del dict2[s2[i]]
            i += 1
        return dict1 == dict2

            





        
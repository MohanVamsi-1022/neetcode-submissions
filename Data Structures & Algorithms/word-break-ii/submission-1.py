class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        words = set(wordDict)
        memo = {}
        def helper(i):
            if i == len(s):
                return [""]
            if i in memo:
                return memo[i]
            res = []
            for j in range(i,len(s)):
                if s[i:j+1] in words:
                    suffix = helper(j+1)
                    for suf in suffix:
                        if suf:
                            res.append(s[i:j+1] + " " + suf)
                        else:
                            res.append(s[i:j+1])
            memo[i] = res
            return res
        return helper(0)


        
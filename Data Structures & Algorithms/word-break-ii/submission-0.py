class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        words = set(wordDict)
        def helper(i,path):
            if i == len(s):
                res.append(" ".join(path))
                return
            for j in range(i,len(s)):
                if s[i:j+1] in words:
                    path.append(s[i:j+1])
                    helper(j+1,path)
                    path.pop()
        helper(0,[])
        return res

        
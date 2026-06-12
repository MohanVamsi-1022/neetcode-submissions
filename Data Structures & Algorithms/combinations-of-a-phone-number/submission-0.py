class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def helper(idx,path):
            if idx == len(digits):
                res.append("".join(path[:]))
                return
            for ch in digitToChar[digits[idx]]:
                path.append(ch)
                helper(idx + 1, path)
                path.pop()
        helper(0,[])
        return res

        
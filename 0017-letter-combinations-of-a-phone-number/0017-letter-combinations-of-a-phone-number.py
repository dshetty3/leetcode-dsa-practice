class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []


        if not digits:
            return res


        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(i, currStr):
            if i == len(digits):
                res.append(''.join(currStr))
                return
        
            for c in  digitToChar[digits[i]]:
                backtrack(i + 1, currStr + c)
        
        if digits:
            backtrack(0, "")
        return res
        


        
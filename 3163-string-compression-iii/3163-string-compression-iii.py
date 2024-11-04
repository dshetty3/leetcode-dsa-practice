class Solution:
    def compressedString(self, word: str) -> str:

        res = ""
        n = len(word)
        left,right = 0,0
        count = 0
        while left < n:
            while right < n and word[left] == word[right]:
                if count == 9:
                    break
                count += 1
                right += 1
            res += (str(count)+word[left])
            left = right
            count = 0
        
        return res
        
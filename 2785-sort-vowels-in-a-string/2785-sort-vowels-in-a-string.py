class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        def isVowel(c):
            return c in 'aeiouAEIOU'
        

        temp = []

        for c in s:
            if isVowel(c):
                temp.append(c)

        temp.sort()

        j = 0
        res = []
        for i in range(len(s)):
            if(isVowel(s[i])):
                res.append(temp[j])
                j += 1
            else:
                res.append(s[i])
        return "".join(res)

        
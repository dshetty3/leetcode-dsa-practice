class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """

        occurence = []
        for i in range(len(s)):
            if s[i] == c:
                occurence.append(i)
        ans = []
        for i in range(len(s)):
            least_distance = []
            for j in occurence:
                least_distance.append(abs(i-j))
            ans.append(min(least_distance))
        return ans


        
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # longest = 0
        # l = 0
        # count = [0] * 26

        # for r in range(len(s)):
        #     count[ord(s[r]) - ord('A')] += 1
        #     while (r-l+1) - max(count) > k:
        #         count[ord(s[l]) - ord('A')] -= 1
        #         l += 1

        #     longest = max(r-l+1, longest)
        # return longest

        charSet = set(s)
        res = 0

        for c in charSet:
            count =  l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
            
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                res = max(res, r - l + 1)
        return res
        
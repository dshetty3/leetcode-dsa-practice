class Solution(object):
    def minMovesToMakePalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        s = list(s)
        while s:
            i = s.index(s[-1])

            if i == len(s) - 1:
                count += (i // 2)  # move to middle of char count 
            else:
                count += i
                s.pop(i)
            
            s.pop()
        return count


        
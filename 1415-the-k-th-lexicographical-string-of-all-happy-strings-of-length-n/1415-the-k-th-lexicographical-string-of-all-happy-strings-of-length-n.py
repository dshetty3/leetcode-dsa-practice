class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        total_happy = 3 * (2 ** (n-1))
        res = []
        choices = "abc"
        left, right = 1, total_happy

        for i in range(n):
            curr = left

            partition = (right - left + 1) // len(choices)

            for c in choices:
                if k in range(curr, curr + partition):
                    res.append(c)
                    left = curr
                    right = curr + partition - 1
                    choices = "abc".replace(c, "")
                    break
                curr += partition
        return "".join(res)


        
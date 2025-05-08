class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """


        ans = []

        while a or b:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                A = ans[-1] =='b'
            else:
                A = a >= b
            
            if A:
                a -= 1
                ans.append('a')
            else:
                b -= 1
                ans.append('b')


        return "".join(ans)
        
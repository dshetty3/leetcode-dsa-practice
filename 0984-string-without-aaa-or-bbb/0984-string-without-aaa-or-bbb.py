class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """


        res = []

        while a or b:
            if a > b:
                if len(res) >= 2 and res[-1] == res[-2] == 'a':
                    res.append('b')
                    b -= 1
                else:
                    res.append('a')
                    a -= 1
            
            else:
                if len(res) >= 2 and res[-1] == res[-2] == 'b':
                    res.append('a')
                    a -= 1
                else:
                    res.append('b')
                    b -= 1
        return ''.join(res)
            # if len(ans) >= 2 and ans[-1] == ans[-2]:
            #     A = ans[-1] =='b'
            # else:
            #     A = a >= b
            
            # if A:
            #     a -= 1
            #     ans.append('a')
            # else:
            #     b -= 1
            #     ans.append('b')


        # return "".join(ans)
        
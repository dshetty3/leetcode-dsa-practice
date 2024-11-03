class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []


        for i in range(left,right+1):
            num = i
            flag = True
            while num > 0:
                digit = num % 10
                if digit == 0 or i % digit != 0:
                    flag = False
                    break
                num //=10
            if flag:
                res.append(i)
        return res



        
        
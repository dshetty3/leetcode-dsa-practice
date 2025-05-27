class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        div = []
        non_div = []

        for i in range(1, n + 1):
            if i % m != 0:
                non_div.append(i)
            else:
                div.append(i)
        
        return sum(non_div) - sum(div)

        
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        five, ten = 0, 0

        for b in bills:
            if b == 5:
                five += 1
            if b == 10:
                ten += 1
        

            change = b - 5

            if change == 5:
                if five > 0:
                    five -= 1
                else:
                    return False

            if change == 15:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

        
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

        num_str = list(str(num))
        max_right = [0] * len(num_str)
        max_right[-1] = len(num_str) - 1


        for i in range(len(num_str) - 2, -1, -1):
            if num_str[i] > num_str[max_right[i + 1]]:
                max_right[i] = i
            else:
                max_right[i] = max_right[i + 1]
        
        for i in range(len(num_str)):
            if num_str[i] != num_str[max_right[i]]:
                num_str[i], num_str[max_right[i]] = num_str[max_right[i]], num_str[i]
                break

        return int(''.join(num_str))



        
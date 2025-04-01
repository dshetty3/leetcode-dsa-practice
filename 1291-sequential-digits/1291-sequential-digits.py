class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """

        res = []
        q = deque(range(1, 10))
        while q:
            n = q.popleft()
            if n > high:
                continue
            if low <= n <= high:
                res.append(n)
            ones = n % 10
            if ones < 9:
                q.append(n * 10 + (ones + 1))
        return res
        
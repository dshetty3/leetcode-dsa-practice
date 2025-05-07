class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """


        circle = deque(range(1, n + 1))

        while len(circle) > 1:
            for i in range(k - 1):
                circle.append(circle.popleft())
            circle.popleft()
        return circle[0]
        
class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """

        res = [0] * len(boxes)
        balls = 0
        moves = 0

        for i in range(len(boxes)):
            res[i] = balls + moves

            moves += balls
            balls += int(boxes[i])

        balls, moves = 0, 0
        for i in reversed(range(len(boxes))):
            res[i] += balls + moves

            moves += balls
            balls += int(boxes[i])  
        return res     
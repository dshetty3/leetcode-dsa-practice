class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """

        start = [0, 0]
        direction = (0, 1) #face north

        for i in instructions:
            if i == 'G':
                start[0] += direction[0]
                start[1] += direction[1]
            elif i == 'L':
                direction = (-direction[1], direction[0])
            elif i == 'R':
                direction = (direction[1], -direction[0])
        
        return start == [0,0] or direction != (0, 1)



        
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """

        q = deque([(0,0,1)]) #disance count to be returned, position, speed
        visit = set()

        while q:
            count, position, speed = q.popleft()
            if position == target:
                return count
            if (position, speed) in visit:
                continue
            visit.add((position, speed))

            q.append((count + 1, position + speed, speed * 2))
            if (position + speed > target and speed > 0) or (position + speed < target and speed < 0):
                speed = - 1 if speed > 0 else 1
                q.append((count + 1, position, speed))

            
            


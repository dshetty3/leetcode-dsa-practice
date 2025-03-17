class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """

        q = deque()

        for i in range(len(tickets)):
            q.append(i)
        
        time = 0

        while q:
            time += 1

            front = q.popleft()
            tickets[front] -= 1
            if k == front and tickets[front] == 0:
                return time
            
            if tickets[front] != 0:
                q.append(front)

        return time

        
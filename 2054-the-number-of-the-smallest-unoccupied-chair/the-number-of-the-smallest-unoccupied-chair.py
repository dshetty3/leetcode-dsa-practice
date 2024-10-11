class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """

        times = [(t[0], t[1], i) for i, t in enumerate(times)]
        times.sort()

        available_chairs = [i for i in range(len(times))]
        used_chair = [] #(l,chair)

        for a,l, i in times:

            while used_chair and used_chair[0][0] <= a:
                leave,chair = heapq.heappop(used_chair)
                heapq.heappush(available_chairs, chair)


            chair = heapq.heappop(available_chairs) #assign chair
            #push in chaires
            heapq.heappush(used_chair, (l,chair)) 

            if i == targetFriend:
                return chair   

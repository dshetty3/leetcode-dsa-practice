class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        count, l, r = 0, 0, len(people) - 1

        while l <= r:
            remain = limit - people[r]
            r -= 1
            count += 1
            if l <= r and remain >= people[l]:
                l += 1
        return count
        
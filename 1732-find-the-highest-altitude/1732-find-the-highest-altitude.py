class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        # current = 0
        # highest = current

        # for h in gain:
        #     current += h
        #     highest = max(highest, current)
        # return highest

        gain1 = [0] 
        height = 0
        for g in gain:
            height += g
            gain1.append(height)
        return max(gain1)







        
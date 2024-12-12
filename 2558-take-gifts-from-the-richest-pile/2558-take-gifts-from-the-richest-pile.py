class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        for _ in range(k):
            large = 0


            for r in range(len(gifts)):
                if gifts[large] < gifts[r]:
                    large = r
    
            gifts[large] = math.floor(
                 math.sqrt(gifts[large])
                 )
        res = sum(gifts)

        return res
        
        
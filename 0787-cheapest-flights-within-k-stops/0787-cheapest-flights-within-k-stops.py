class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tempP = prices.copy()
            for s, d, cost in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + cost < tempP[d]:
                    tempP[d] = prices[s] + cost
            prices = tempP
        return -1 if prices[dst] == float("inf") else prices[dst]
        
class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """

        count = Counter(barcodes)
        

        maxHeap = [(-freq, barcode) for barcode, freq in count.items()]
        heapq.heapify(maxHeap)

        prev = None 
        res = []

        while maxHeap or prev:
            
            if not maxHeap and prev:
                return []
            
            freq, barcode = heapq.heappop(maxHeap)
            res.append(barcode)
            freq += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if freq != 0:
                prev = (freq, barcode)
        
        return res


        
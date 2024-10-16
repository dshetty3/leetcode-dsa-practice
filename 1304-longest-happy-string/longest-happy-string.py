class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        heap = []
    
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        
        result = []
        
        while heap:
            first_count, first_char = heapq.heappop(heap)
            
            # If we can add the most frequent character without violating the "happy" rule
            if len(result) >= 2 and result[-1] == result[-2] == first_char:
                if not heap:
                    break
                # Use the next most frequent character instead
                second_count, second_char = heapq.heappop(heap)
                result.append(second_char)
                second_count += 1  # Since we are using a max-heap with negative counts
                
                # If there are still some of second_char left, push it back to the heap
                if second_count < 0:
                    heapq.heappush(heap, (second_count, second_char))
                
                # Push the first character back to the heap
                heapq.heappush(heap, (first_count, first_char))
            else:
                # Add the most frequent character
                result.append(first_char)
                first_count += 1  # Since we are using a max-heap with negative counts
                
                # If there are still some of first_char left, push it back to the heap
                if first_count < 0:
                    heapq.heappush(heap, (first_count, first_char))
        
        return ''.join(result)
            
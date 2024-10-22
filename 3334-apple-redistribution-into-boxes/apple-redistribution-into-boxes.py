class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:

        total = sum(apple)
        capacity.sort(reverse=True)
        num_boxes = 0

        for n in capacity:
            total -= n
            num_boxes += 1
            if total <= 0:
                return num_boxes
        

        
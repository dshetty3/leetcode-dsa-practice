class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_no = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = max_no
            if temp > max_no:
                max_no = temp   
        return arr
        
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        res = [-1]
        max_no = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            res.append(max_no)
            if arr[i] > max_no:
                max_no = arr[i]
        res.reverse()
        return res

        
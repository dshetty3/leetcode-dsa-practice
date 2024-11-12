class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []

        for n in arr2:
            for j in range(len(arr1)):
                if arr1[j] == n:
                    res.append(arr1[j])
                    arr1[j] = -1
        arr1.sort()

        for v in arr1:
            if v != -1:
                res.append(v)
        return res
        
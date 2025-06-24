func findKDistantIndices(nums []int, key int, k int) []int {

    var res []int
    r := 0

    for j:=0; j < len(nums); j++ {
        if nums[j] == key{
            l := max(r, j - k)
            r = min(len(nums) - 1, j + k) + 1
            for i := l; i < r; i++ {
                res = append(res, i)
            }
        }

    }
    return res
    
}
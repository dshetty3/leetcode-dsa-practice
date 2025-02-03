/**
 * @param {number[]} nums
 * @return {number}
 */
var longestMonotonicSubarray = function(nums) {
    
    let cur = 1
    let res = 1
    let increasing = 0

    for(let i = 1; i < nums.length; i++){
        if (nums[i-1] < nums[i]){
            if (increasing > 0){
                cur += 1 
            } else{
                cur = 2
                increasing = 1
            }
        } else if (nums[i-1] > nums[i]){
            if (increasing < 0){
                cur += 1
            } else {
                cur = 2
                increasing = -1
            }
        } else {
            cur = 1
            increasing = 1
        }

        res = Math.max(res, cur)
    }
    return res

};
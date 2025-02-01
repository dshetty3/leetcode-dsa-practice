/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {

    let curr_sum = 0
    let max_sum = -Infinity;

    for(let i = 0; i < nums.length; i++){
        curr_sum += nums[i];
        max_sum = Math.max(max_sum, curr_sum)
        if (curr_sum < 0) {
            curr_sum = 0
    }
    }
    return max_sum
    
};
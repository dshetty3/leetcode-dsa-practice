/**
 * @param {number[]} nums
 * @return {number}
 */
var longestMonotonicSubarray = function(nums) {
    if (nums.length === 0) return 0;

    let cur = 1;
    let res = 1;
    let increase = 0;

    for (let i = 1; i < nums.length; i++) {
        if (nums[i - 1] < nums[i]) {
            if (increase > 0) {
                cur += 1;
            } else {
                cur = 2;
                increase = 1;
            }
        } else if (nums[i - 1] > nums[i]) {
            if (increase < 0) {
                cur += 1;
            } else {
                cur = 2;
                increase = -1;
            }
        } else {
            cur = 1;
            increase = 0;
        }
        res = Math.max(res, cur);
    }

    return res;
};

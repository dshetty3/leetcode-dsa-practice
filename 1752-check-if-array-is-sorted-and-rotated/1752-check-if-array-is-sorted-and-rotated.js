/**
 * @param {number[]} nums
 * @return {boolean}
 */
var check = function(nums) {
    

    let count = 1;
    const N = nums.length;

    if(N === 1){
        return true
    }

    for (let i = 1; i < 2 * N; i++){
        if (nums[(i - 1) % N] <= nums[i % N]){
            count++;
        }else count = 1
        if (count === N) return true
    }
    return false

};
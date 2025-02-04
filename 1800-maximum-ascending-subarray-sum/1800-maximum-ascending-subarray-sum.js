/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAscendingSum = function(nums) {

   let curr = nums[0];
   let res = curr;

   for(let i = 0; i < nums.length; i++){
        if(nums[i - 1] < nums[i]){
            curr += nums[i];
        } else {
            curr = nums[i];
        }
        res = Math.max(res, curr);
   }
    return res;
};
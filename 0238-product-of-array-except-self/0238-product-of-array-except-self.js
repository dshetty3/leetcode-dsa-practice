/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {

    const res = new Array(nums.length).fill(1);

    var prefix = 1
    for (let i = 0; i < nums.length; i++){
        res[i] = prefix
        prefix *= nums[i]
    }

    var postfix = 1
    for (let i = nums.length - 1; i >= 0; i--){
        res[i] *= postfix
        postfix *= nums[i]
    }

    return res
    
};


//  res = [1] * (len(nums))

//         prefix = 1
//         for i in range(len(nums)):
//             res[i] = prefix
//             prefix *= nums[i]
        
//         postfix = 1
//         for i in range(len(nums)-1, -1, -1): 
//             res[i] *= postfix
//             postfix *= nums[i]
//         return res
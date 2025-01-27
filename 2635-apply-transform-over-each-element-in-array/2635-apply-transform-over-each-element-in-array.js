/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let res = [];

    for (const i in arr){
        res.push(fn(arr[i], Number(i))); // if string - will throw error. { name: "Disha", number: 7
        }
    }
    
    return res;
    
};
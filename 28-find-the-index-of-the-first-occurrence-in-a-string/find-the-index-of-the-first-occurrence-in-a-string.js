/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {

    for (let i = 0; i < haystack.length; i++){ //i is for haystack and j is to expand our serach in haystack
        let j 
        for(j = 0; j < needle.length; j++){
            if (haystack[i + j] != needle[j])
                break
        }
         if(j === needle.length){
                return i
         }
    }
    return -1  
};
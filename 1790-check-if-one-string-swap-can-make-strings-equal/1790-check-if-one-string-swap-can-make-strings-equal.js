/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var areAlmostEqual = function(s1, s2) {
    let index = []

    for(let i = 0; i < s1.length; i++){
        if (s1[i] != s2[i]) {index.push(i);
        if (index.length > 2) return false;}
        }
         if (index.length === 2){
            let [i, j] = index;
            return s1[i] === s2[j] && s2[i] === s1[j];
        } 
        return index.length === 0;

    };
    

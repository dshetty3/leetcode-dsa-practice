/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {

    if(Array.isArray(obj)){
        return obj.map(compactObject).filter(Boolean)
    } else if (obj != null && typeof obj === 'object'){
        for (let key in obj){
            if(obj.hasOwnProperty(key)){
                obj[key] = compactObject(obj[key]);
                if (!obj[key]){
                    delete obj[key]
                }
            }
        }
    }
    return obj;



    
};


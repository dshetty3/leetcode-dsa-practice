/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World";
    };
}

const a = createHelloWorld();
console.log(a());

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
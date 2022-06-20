/**
 * https://leetcode.com/problems/fibonacci-number/
 */


/**
 * @param {number} n
 * @return {number}
 */

var fib = function(n) {
    let sequence = [0, 1];
    if (n <= 1) {
        return n;
    };

    var curr = 1;

    while (!(curr == n)) {
        sequence.push(sequence.at(-1) + sequence.at(-2));
        console.log(sequence);
        curr += 1;
        sequence.shift();
    };
    return sequence.slice(-1);
};


console.log(fib(3));

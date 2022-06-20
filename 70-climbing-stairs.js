/**
 * https://leetcode.com/problems/climbing-stairs/
 */

/**
 * @param {number} n
 * @return {number}
 */


var climbStairs = function(n) {
    let ways = [1, 2];
    
    if (n <= 2) {
        return n;
    };

    let curr = 2;
    while (!(curr == n)) {
        ways.push(ways.at(-2) + ways.at(-1));
        // Always keep array of size 2
        ways.shift();
        curr += 1;
    };

    return ways.at(-1);
};

console.log(climbStairs(3));
console.log(climbStairs(10));
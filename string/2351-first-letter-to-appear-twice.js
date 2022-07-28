/**
 * https://leetcode.com/problems/first-letter-to-appear-twice/
 */

const { c } = require("tar");


var repeatedCharacter = function(s) {
    let seen = new Set();
    
    for (c of s) {
        if (seen.has(c)) {
            return c;
        }
        seen.add(c);
    }
};


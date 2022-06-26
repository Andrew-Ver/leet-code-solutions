/**
 * https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/
 */


/**
 * @param {string} s
 * @return {string}
 */

var greatestLetter = function(s) {
    let greatest = 0;
    let seen = new Set();

    for (i in s) {
        let curr = s.charCodeAt(i);
        if ((seen.has(curr-32)) && (curr-32 > greatest)){
            greatest = curr-32;
        } else if ((seen.has(curr+32) && (curr > greatest))) {
            greatest = curr;
        }
        seen.add(curr);
    };
    if (greatest == 0) {
        return '';
    }
    return String.fromCharCode(greatest);
};


console.log(greatestLetter("arRAzFif"));
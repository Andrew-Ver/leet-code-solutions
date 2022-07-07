/*
*   https://leetcode.com/problems/decode-the-message/
*/


/**
 * @param {string} key
 * @param {string} message
 * @return {string}
 */

var decodeMessage = function(key, message) {
    let currCharCode = 97;
    const mappings = {' ': ' '};

    for (i in key) {
        if (!(key[i] === ' ') && (!(key[i] in mappings))) {
            mappings[key[i]] = String.fromCharCode(currCharCode);
            currCharCode += 1;
        }
    }

    let decoded = '';

    for (letter of message) {
        decoded += mappings[letter];
    }
    
    return decoded
};

console.log(decodeMessage(key = "the quick brown fox jumps over the lazy dog", 
                            message = "vkbs bs t suepuv"));
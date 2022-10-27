/**
 *  https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
 * 
 * Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
 * Return the positive integer k. If there is no such integer, return -1.
 */


var findMaxK = function(nums){
    let largest_so_far = -1;
    let s = new Set();

    for (n of nums){
        if (s.has(-n) && (Math.abs(n) >largest_so_far)) {
            largest_so_far = Math.abs(n);
        }
        s.add(n);
    }
    return largest_so_far;
};


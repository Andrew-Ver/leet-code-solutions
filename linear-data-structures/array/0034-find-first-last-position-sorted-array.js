/*
* https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */


var searchRange = function(nums, target) {
    let i = 0;
    let j = nums.length-1;
    
    let firstPos = -1;
    let endPos = -1;

    while (i <= j) {
        if (nums[i] == target) {
            if ((firstPos == -1) || i < firstPos) {
                firstPos = i;
            } 
        
            if ((endPos === -1) || (i > endPos)) {
                endPos = i;
            }
        };
    
        if (nums[j] == target) {
            if ((endPos === -1) || j > endPos) {
                endPos = j;
            } 
            if ((firstPos == -1) || (j < firstPos)) {
                firstPos = j;
            }            
        };
        
        i += 1;
        j -= 1;
    };

    return Array(firstPos, endPos);
    
};


console.log(searchRange(nums = [2, 2], target = 2));

console.log(searchRange(nums = [0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10], target = 4));
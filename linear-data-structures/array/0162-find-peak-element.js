/**
 * https://leetcode.com/problems/find-peak-element/
 */


/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    let i = 1;
    let j = nums.length-2;

    while (i <= j) {
        if (nums[i-1] < nums[i] && nums[i+1] < nums[i]) {
            return i;
        }

        if (nums[j-1] < nums[j] && nums[j+1] < nums[j]) {
            return j;
        }

        i += 1;
        j -= 1;
    }

};
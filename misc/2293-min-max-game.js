/** 
 * https://leetcode.com/problems/min-max-game/
*/


var minMaxGame = function(nums) {
    var i = 0;
    var min_check = true;

    while (nums.length != 1) {
        if (i >= nums.length) {
            i = 0;
        }

        if (min_check) {
            min_check = false;
            if (nums[i] < nums[i+1]) {
                nums.splice(i+1, 1);
            } else {
                nums.splice(i, 1);
            }

        } else if (!min_check) {
            min_check = true;
            if (nums[i] > nums[i+1]) {
                nums.splice(i+1, 1);
            } else {
                nums.splice(i, 1);
            }
        }   nums.splice()
        i += 1
    }

    return nums[0];
};


console.log(minMaxGame([1,3,5,2,4,8,2,2]));
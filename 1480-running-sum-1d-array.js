/** 
    https://leetcode.com/problems/running-sum-of-1d-array/
*/


var runningSum = function(nums) {
    let prev = 0;
    let ans = [];
    
    for (let n of nums){
        ans.push(n+prev);
        prev += n;
    }
    return ans;
}

console.log(runningSum([1, 2, 3, 4]));
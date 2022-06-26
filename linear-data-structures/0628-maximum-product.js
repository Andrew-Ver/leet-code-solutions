/*
*   https://leetcode.com/problems/maximum-product-of-three-numbers/
*/



var maximumProduct = function(nums) {
    /**
     * @param {number[]} nums
     * @return {number}
    */
    nums.sort((a,b) => (b-a));

    let ans = [];
    let positives = [];
    let negatives = [];

    for (num of nums) {
        if (num > 0) {
            positives.push(num);
        } else if (num < 0) {
            negatives.push(num);
        };
    };
    
    if (!negatives.length) {
        ans = ans.concat(positives.slice(0, 3));    
    } else if (!positives.length) {
        ans = ans.concat(negatives.slice(-3, ));
    } else if (negatives.length > 2) {
        
    }

    return ans.reduce((a, b) => a*b, initalValue=1);
};  

console.log(maximumProduct([-1, -2, -3]));

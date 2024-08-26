/*
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6
 
Constraints:
3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumProduct = function (nums) {
    let sortedNums = nums.sort((a, b) => b - a);

    let max1 = sortedNums[0] * sortedNums[1] * sortedNums[2];
    let max2 = sortedNums[sortedNums.length - 1] * sortedNums[sortedNums.length - 2] * sortedNums[0];

    return Math.max(max1, max2);
};

let nums = [1, 2, 3, 4];
console.log(maximumProduct(nums));
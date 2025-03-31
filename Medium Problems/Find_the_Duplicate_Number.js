/*
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function (nums) {
    let count = {};

    for (let num of nums) {
        if (num in count) {
            count[num] += 1;
        } else {
            count[num] = 1;
        }
    }
    for (let [key, value] of Object.entries(count)) {
        if (value >= 2) {
            return parseInt(key);
        }
    }
};


let nums = [1, 3, 4, 2, 2];
console.log(findDuplicate(nums));
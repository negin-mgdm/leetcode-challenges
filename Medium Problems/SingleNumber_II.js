/*
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
 
Constraints:
1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
    let count = {};

    for (let num of nums) {
        if (count[num] != undefined) {
            count[num] += 1;
        } else {
            count[num] = 1;
        }
    }

    for (let num of nums) {
        if (count[num] == 1) {
            return num;
        }
    }
};

let nums = [2, 2, 3, 2];
console.log(singleNumber(nums));
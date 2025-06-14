/*
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 
Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function (nums, target) {
    let result = [-1, -1];

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == target) {
            result[0] = i;
            break;
        }
    }

    for (let i = nums.length - 1; i >= 0; i--) {
        if (nums[i] == target) {
            result[1] = i;
            break;
        }
    }

    return result;
};

let nums = [5, 7, 7, 8, 8, 10];
let target = 8;
console.log(searchRange(nums, target));
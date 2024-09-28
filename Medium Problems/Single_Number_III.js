/*
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]

Example 3:
Input: nums = [0,1]
Output: [1,0]
 
Constraints:
2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function (nums) {
    let count = {};
    for (let num of nums) {
        if (num in count) {
            count[num] += 1;
        } else {
            count[num] = 1;
        }
    }
    let result = [];
    for (let [key, value] of Object.entries(count)) {
        if (value == 1) {
            result.push(parseInt(key));
        }
    }
    return result;
};

let nums = [1, 2, 1, 3, 2, 5];
console.log(singleNumber(nums));
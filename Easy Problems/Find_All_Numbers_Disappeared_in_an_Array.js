/*
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]
 
Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function (nums) {
    let output = [];
    let n = nums.length;
    let arr = new Set(nums);

    for (let i = 1; i < n + 1; i++) {
        if (!arr.has(i)) {
            output.push(i);
        }
    }
    return output;
};

let nums = [4, 3, 2, 7, 8, 2, 3, 1];
console.log(findDisappearedNumbers(nums));
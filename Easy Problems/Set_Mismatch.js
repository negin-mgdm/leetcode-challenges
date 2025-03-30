/*
You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, 
which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]
 
Constraints:
2 <= nums.length <= 104
1 <= nums[i] <= 104
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function (nums) {
    let sortedNums = nums.sort((a, b) => a - b);
    let sumOfNums = nums.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    let uniqueNums = new Set(nums);
    let sumOfUniqueNums = Array.from(uniqueNums).reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    let missingNum = sumOfNums - sumOfUniqueNums;

    let result = [missingNum];
    for (let i = 1; i < sortedNums.length + 1; i++) {
        if (!uniqueNums.has(i)) {
            result.push(i);
            break;
        }
    }

    return result;
};

let nums = [1, 2, 2, 4];
console.log(findErrorNums(nums));
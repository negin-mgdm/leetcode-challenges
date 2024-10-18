/*
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and 
the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, 
then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

Example 1:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

Example 2:
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

Example 3:
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
 
Constraints:
1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums is sorted in a non-decreasing order.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumCount = function (nums) {
    let count = {};
    let pos = 0;
    let neg = 0;

    for (let num of nums) {
        if (num in count) {
            count[num] += 1;
        }
        else {
            count[num] = 1;
        }
    }

    for (let [key, value] of Object.entries(count)) {
        if (key > 0) {
            pos += value;
        }
        else if (key < 0) {
            neg += value;
        }

    }

    return Math.max(pos, neg);
};

let nums = [-3, -2, -1, 0, 0, 1, 2];
console.log(maximumCount(nums));

/*
var maximumCount = function (nums) {
    let pos = 0;
    let neg = 0;
    for (let num of nums) {
        if (num > 0) {
            pos += 1;
        }
        else if (num < 0) {
            neg += 1;
        }
    }

    if (pos > neg) {
        return pos;
    }
    else if (neg > pos) {
        return neg;
    } else {
        return pos;
    }
};
*/
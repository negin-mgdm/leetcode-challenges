/*
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"
*/

/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function (nums) {
    let numStr = [];
    for (let num of nums) {
        numStr.push(num.toString());
    }

    for (let i = 0; i < numStr.length; i++) {
        for (let j = i + 1; j < numStr.length; j++) {
            if (numStr[i] + numStr[j] < numStr[j] + numStr[i]) {
                // Swap the elements if the condition is met.
                let temp = numStr[i];
                numStr[i] = numStr[j];
                numStr[j] = temp;
            }
        }
    }
    let result = numStr.join("");
    if (result[0] == "0") {
        return "0";
    }
    return result;
};

let nums = [3, 30, 34, 5, 9];
console.log(largestNumber(nums));

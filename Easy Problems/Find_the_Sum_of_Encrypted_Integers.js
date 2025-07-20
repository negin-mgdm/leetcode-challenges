/*
You are given an integer array nums containing positive integers.
We define a function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x. 
For example, encrypt(523) = 555 and encrypt(213) = 333.
Return the sum of encrypted elements.

Example 1:
Input: nums = [1,2,3]
Output: 6
Explanation: The encrypted elements are [1,2,3]. The sum of encrypted elements is 1 + 2 + 3 == 6.

Example 2:
Input: nums = [10,21,31]
Output: 66
Explanation: The encrypted elements are [11,22,33]. The sum of encrypted elements is 11 + 22 + 33 == 66.

Constraints:
1 <= nums.length <= 50
1 <= nums[i] <= 1000
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfEncryptedInt = function (nums) {
    let result = [];
    for (let num of nums) {
        let n = num.toString();
        let maxDigit = Math.max(...n.split('').map(Number));
        let numLength = n.length;
        let encryptedValue = Number(maxDigit.toString().repeat(n.length));
        result.push(Number(encryptedValue));
    }
    return result.reduce((accumulator, current) => accumulator + current, 0);
};

const nums = [10, 21, 31];
console.log(sumOfEncryptedInt(nums));
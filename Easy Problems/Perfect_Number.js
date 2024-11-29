/*
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. 
A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:
Input: num = 7
Output: false
 
Constraints:
1 <= num <= 108
*/

/**
 * @param {number} num
 * @return {boolean}
 */
var checkPerfectNumber = function (num) {
    if (num == 1) {
        return false;
    }
    let divisors = 1;
    for (let i = 2; i < parseInt(num ** 0.5) + 1; i++) {
        if (num % i == 0) {
            divisors += i;
            if (i != Math.floor(num / i)) {
                divisors += Math.floor(num / i);
            }
        }
    }
    return num == divisors;
};

let num = 28;
console.log(checkPerfectNumber(num));
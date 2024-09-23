/*
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:
Input: n = 3
Output: [-1,0,1]

Example 3:
Input: n = 1
Output: [0]
 
Constraints:
1 <= n <= 1000
*/

/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function (n) {
    let x = Math.floor(n / 2);

    let nums = []

    for (let i = 1; i <= x; i++) {
        nums.push(-i);
        nums.push(i);
    }

    if (n % 2 != 0) {
        nums.push(0);
    }
    return nums;
};

let n = 5;
console.log(sumZero(n));




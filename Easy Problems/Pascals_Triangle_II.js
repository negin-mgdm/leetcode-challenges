/*
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
 
Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Constraints:
0 <= rowIndex <= 33
*/
/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function (rowIndex) {
    let prev = [1];
    for (let n = 1; n <= rowIndex; n++) {
        let row = new Array(n + 1).fill(1);
        let mid = Math.floor(n / 2);
        for (let j = 1; j <= mid; j++) {
            let val = prev[j - 1] + prev[j];
            row[j] = val;
            row[n - j] = val;
        }
        prev = row;
    }
    return prev;
};

const rowIndex = 3;
console.log(getRow(rowIndex));
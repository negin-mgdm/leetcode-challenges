/*
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
 
Constraints:
1 <= numRows <= 30
*/

/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
    if (numRows == 1) {
        return [[1]];
    }

    const rows = [[1]];
    numRows -= 1;

    while (numRows != 0) {
        const above = rows[rows.length - 1];
        const row = [1];
        for (let i = 0; i < above.length - 1; i++) {
            row.push(above[i] + above[i + 1]);
        }
        row.push(1);
        rows.push(row);
        numRows -= 1;
    }

    return rows;
};

const numRows = 5;
console.log(generate(numRows));
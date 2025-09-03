/*
You are given an n x n integer matrix grid.
Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
Return the generated matrix.

Example 1:
Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.

Example 2:
Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
Output: [[2,2,2],[2,2,2],[2,2,2]]
Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.
 
Constraints:
n == grid.length == grid[i].length
3 <= n <= 100
1 <= grid[i][j] <= 100
*/

/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var largestLocal = function (grid) {
    const n = grid.length;
    const res = Array.from({ length: n - 2 }, () => Array(n - 2).fill(0));

    for (let i = 1; i < n - 1; i++) {
        for (let j = 1; j < n - 1; j++) {
            let maxVal = -Infinity;
            for (let x = i - 1; x <= i + 1; x++) {
                for (let y = j - 1; y <= j + 1; y++) {
                    if (grid[x][y] > maxVal) {
                        maxVal = grid[x][y];
                    }
                }
            }
            res[i - 1][j - 1] = maxVal;
        }
    }

    return res;
};

const grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]];
console.log(largestLocal(grid));
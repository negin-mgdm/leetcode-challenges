/*
You are given a 2D matrix grid of size m x n. You need to check if each cell grid[i][j] is:
Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
Return true if all the cells satisfy these conditions, otherwise, return false.

Example 1:
Input: grid = [[1,0,2],[1,0,2]]
Output: true

Example 2:
Input: grid = [[1,1,1],[0,0,0]]
Output: false

Example 3:
Input: grid = [[1],[2],[3]]
Output: false

Constraints:
1 <= n, m <= 10
0 <= grid[i][j] <= 9
*/

/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var satisfiesConditions = function (grid) {
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (i + 1 < grid.length && grid[i][j] != grid[i + 1][j]) {
                return false;
            }
            if (j + 1 < grid[i].length && grid[i][j] == grid[i][j + 1]) {
                return false;
            }
        }
    }
    return true;
};

let grid = [[1, 0, 2], [1, 0, 2]];
console.log(satisfiesConditions(grid));
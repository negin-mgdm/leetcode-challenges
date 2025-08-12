/*
There is a snake in an n x n matrix grid and can move in four possible directions. 
Each cell in the grid is identified by the position: grid[i][j] = (i * n) + j.
The snake starts at cell 0 and follows a sequence of commands.
You are given an integer n representing the size of the grid and an array of strings commands where each command[i] is either "UP", "RIGHT", "DOWN", and "LEFT". 
It's guaranteed that the snake will remain within the grid boundaries throughout its movement.
Return the position of the final cell where the snake ends up after executing commands.

Example 1:
Input: n = 2, commands = ["RIGHT","DOWN"]
Output: 3

Example 2:
Input: n = 3, commands = ["DOWN","RIGHT","UP"]
Output: 1

Constraints:
2 <= n <= 10
1 <= commands.length <= 100
commands consists only of "UP", "RIGHT", "DOWN", and "LEFT".
The input is generated such the snake will not move outside of the boundaries.
*/

/**
 * @param {number} n
 * @param {string[]} commands
 * @return {number}
 */
var finalPositionOfSnake = function (n, commands) {
    let matrix = [];
    for (let i = 0; i < n; i++) {
        let row = [];
        for (let j = 0; j < n; j++) {
            row.push(i * n + j);
        }
        matrix.push(row);
    }

    let row = 0;
    let col = 0;
    for (let position of commands) {
        if (position == "RIGHT") {
            col += 1;
        }
        else if (position == "LEFT") {
            col -= 1;
        }
        else if (position == "UP") {
            row -= 1;
        }
        else if (position == "DOWN") {
            row += 1;
        }
    }
    return matrix[row][col];
};

const n = 2;
const commands = ["RIGHT", "DOWN"];
console.log(finalPositionOfSnake(n, commands));



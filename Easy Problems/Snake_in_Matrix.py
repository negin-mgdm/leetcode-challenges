'''
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
'''
from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(i * n + j)
            matrix.append(row)

        row = 0
        col = 0
        for position in commands:
            if position == "RIGHT":
                col += 1
            elif position == "LEFT":
                col -= 1
            elif position == "UP":
                row -= 1
            elif position == "DOWN":
                row += 1

        return matrix[row][col]


n = 2
commands = ["RIGHT", "LEFT"]
solution = Solution()
print(solution.finalPositionOfSnake(n, commands))

'''
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
'''


from typing import List


class Solution(object):
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        for n in range(1, rowIndex + 1):
            row = [1] * (n + 1)
            mid = n // 2
            for j in range(1, mid + 1):
                val = prev[j - 1] + prev[j]
                row[j] = val
                row[n - j] = val
            prev = row
        return prev


solution = Solution()
index = 5
row = solution.getRow(index)
print(row)

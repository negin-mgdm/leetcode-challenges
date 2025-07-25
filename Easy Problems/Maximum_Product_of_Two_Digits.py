'''
You are given a positive integer n.
Return the maximum product of any two digits in n.
Note: You may use the same digit twice if it appears more than once in n.

Example 1:
Input: n = 31
Output: 3
Explanation:
The digits of n are [3, 1].
The possible products of any two digits are: 3 * 1 = 3.
The maximum product is 3.

Example 2:
Input: n = 22
Output: 4
Explanation:
The digits of n are [2, 2].
The possible products of any two digits are: 2 * 2 = 4.
The maximum product is 4.

Example 3:
Input: n = 124
Output: 8
Explanation:
The digits of n are [1, 2, 4].
The possible products of any two digits are: 1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8.
The maximum product is 8.

Constraints:
10 <= n <= 109
'''


class Solution:
    def maxProduct(self, n: int) -> int:
        number = sorted(str(n))
        max_product = 1

        max_product *= int(number[-1])
        max_product *= int(number[-2])

        return max_product


n = 124
solution = Solution()
print(solution.maxProduct(n))

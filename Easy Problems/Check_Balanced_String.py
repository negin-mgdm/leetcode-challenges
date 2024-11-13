'''
You are given a string num consisting of only digits. 
A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.

Return true if num is balanced, otherwise return false.

Example 1:
Input: num = "1234"
Output: false
Explanation:
The sum of digits at even indices is 1 + 3 == 4, and the sum of digits at odd indices is 2 + 4 == 6.
Since 4 is not equal to 6, num is not balanced.

Example 2:
Input: num = "24123"
Output: true
Explanation:
The sum of digits at even indices is 2 + 1 + 3 == 6, and the sum of digits at odd indices is 4 + 2 == 6.
Since both are equal the num is balanced.
 
Constraints:
2 <= num.length <= 100
num consists of digits only
'''


class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        sum_of_even_digits = 0
        sum_of_odd_digits = 0

        for i, digit in enumerate(num):
            if i % 2 == 0:
                sum_of_even_digits += int(digit)
            if i % 2 != 0:
                sum_of_odd_digits += int(digit)

        return sum_of_even_digits == sum_of_odd_digits


num = "24123"
solution = Solution()
print(solution.isBalanced(num))

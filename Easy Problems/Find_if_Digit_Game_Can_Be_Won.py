'''
You are given an array of positive integers nums.
Alice and Bob are playing a game. 
In the game, Alice can choose either all single-digit numbers or all double-digit numbers from nums, 
and the rest of the numbers are given to Bob. Alice wins if the sum of her numbers is strictly greater than the sum of Bob's numbers.

Return true if Alice can win this game, otherwise, return false.

Example 1:
Input: nums = [1,2,3,4,10]
Output: false
Explanation:
Alice cannot win by choosing either single-digit or double-digit numbers.

Example 2:
Input: nums = [1,2,3,4,5,14]
Output: true
Explanation:
Alice can win by choosing single-digit numbers which have a sum equal to 15.

Example 3:
Input: nums = [5,5,5,25]
Output: true
Explanation:
Alice can win by choosing double-digit numbers which have a sum equal to 25.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 99
'''

# Solution 1:


class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        double_digits = 0
        single_digits = 0

        for num in nums:
            if len(str(num)) == 1:
                single_digits += num
            else:
                double_digits += num

        if double_digits == single_digits:
            return False
        else:
            return True


nums = [5, 5, 5, 25]
solution = Solution()
print(solution.canAliceWin(nums))


# Solution 2:

class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        double_digits = 0
        single_digits = 0

        for num in nums:
            if num < 10:
                single_digits += num
            else:
                double_digits += num

        return double_digits != single_digits


nums = [1, 2, 3, 4, 5, 14]
solution = Solution()
print(solution.canAliceWin(nums))

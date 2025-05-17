'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
'''

from collections import Counter


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 'You must implement a solution with a linear runtime complexity and use only constant extra space.' harder that I expected, decided to ignore this :)
        count = Counter(nums)

        for num in nums:
            if count[num] == 1:
                return num


nums = [0, 1, 0, 1, 0, 1, 99]
solution = Solution()
print(solution.singleNumber(nums))

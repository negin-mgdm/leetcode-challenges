'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6
 
Constraints:
3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
'''


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums, reverse=True)

        # Consider the product of the three largest numbers.
        max1 = sorted_nums[0] * sorted_nums[1] * sorted_nums[2]

        # Consider the product of the two smallest numbers (could be very negative) and the largest number.
        max2 = sorted_nums[-1] * sorted_nums[-2] * sorted_nums[0]

        # return the larger of these two possible products.
        return max(max1, max2)


nums = [-100, -98, -1, 2, 3, 4]
solution = Solution()
print(solution.maximumProduct(nums))

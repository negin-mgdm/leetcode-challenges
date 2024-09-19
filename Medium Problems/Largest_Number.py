'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"
'''


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums_str = []
        for num in nums:
            nums_str.append(str(num))

        for i in range(len(nums_str)):
            for j in range(i + 1, len(nums_str)):
                if nums_str[i] + nums_str[j] < nums_str[j] + nums_str[i]:
                    # Swap the elements to ensure the larger concatenation comes first.
                    nums_str[i], nums_str[j] = nums_str[j], nums_str[i]

        result = ''.join(nums_str)

        if result[0] == '0':
            return '0'

        return result


nums = [3, 30, 34, 5, 9]
solution = Solution()
print(solution.largestNumber(nums))

'''
You are given an integer array nums containing positive integers.
We define a function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x. 
For example, encrypt(523) = 555 and encrypt(213) = 333.
Return the sum of encrypted elements.

Example 1:
Input: nums = [1,2,3]
Output: 6
Explanation: The encrypted elements are [1,2,3]. The sum of encrypted elements is 1 + 2 + 3 == 6.

Example 2:
Input: nums = [10,21,31]
Output: 66
Explanation: The encrypted elements are [11,22,33]. The sum of encrypted elements is 11 + 22 + 33 == 66.

Constraints:
1 <= nums.length <= 50
1 <= nums[i] <= 1000
'''
from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        result = []

        for num in nums:
            n = str(num)
            max_digit = max(n)
            num_length = len(n)
            encrypted_value = max_digit * num_length
            result.append(int(encrypted_value))

        return sum(result)


nums = [10, 21, 31]
solution = Solution()
print(solution.sumOfEncryptedInt(nums))

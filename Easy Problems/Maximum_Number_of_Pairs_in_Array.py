'''
You are given a 0-indexed integer array nums. In one operation, you may do the following:

Choose two integers in nums that are equal.
Remove both integers from nums, forming a pair.
The operation is done on nums as many times as possible.

Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that 
are formed and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.

Example 1:
Input: nums = [1,3,2,1,3,2,2]
Output: [3,1]
Explanation:
Form a pair with nums[0] and nums[3] and remove them from nums. Now, nums = [3,2,3,2,2].
Form a pair with nums[0] and nums[2] and remove them from nums. Now, nums = [2,2,2].
Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [2].
No more pairs can be formed. A total of 3 pairs have been formed, and there is 1 number leftover in nums.

Example 2:
Input: nums = [1,1]
Output: [1,0]
Explanation: Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [].
No more pairs can be formed. A total of 1 pair has been formed, and there are 0 numbers leftover in nums.

Example 3:
Input: nums = [0]
Output: [0,1]
Explanation: No pairs can be formed, and there is 1 number leftover in nums.
 
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
'''
from collections import Counter


class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)

        i = 0
        pair_count = 0
        leftover_nums = 0

        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                pair_count += 1
                i += 2
            else:
                leftover_nums += 1
                i += 1

        # If there's one leftover number at the end.
        if i == len(nums) - 1:
            leftover_nums += 1

        return [pair_count, leftover_nums]


nums = [1, 3, 2, 1, 3, 2, 2]
solution = Solution()
print(solution.numberOfPairs(nums))

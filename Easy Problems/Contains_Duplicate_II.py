'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_map = {}

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i

        return False


nums = [1, 2, 3, 1, 2, 3]
k = 2
solution = Solution()
print(solution.containsNearbyDuplicate(nums, k))

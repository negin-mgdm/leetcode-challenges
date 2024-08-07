'''
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 
Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''

# Optimised Solution:


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        shorter_arr = set(nums1 if len(nums1) <= len(nums2) else nums2)
        longer_arr = set(nums1 if len(nums1) > len(nums2) else nums2)

        result = []
        for i in shorter_arr:
            if i in longer_arr:
                result.append(i)

        return result


nums1 = [3]
nums2 = [1]
solution = Solution()
print(solution.intersection(nums1, nums2))


# First submitted Solution:
class Solution(object):
    def intersection1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            shorter_arr = nums1
            longer_arr = nums2
        else:
            shorter_arr = nums2
            longer_arr = nums1

        shorter_arr = set(shorter_arr)
        longer_arr = set(longer_arr)

        result = []
        for i in shorter_arr:
            for j in longer_arr:
                if i == j:
                    result.append(i)

        return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
solution = Solution()
print(solution.intersection1(nums1, nums2))

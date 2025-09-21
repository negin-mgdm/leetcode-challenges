'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
'''
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums: List[int], low: int, high: int) -> Optional[TreeNode]:
        if low > high:
            return None
        mid = (low + high) // 2
        node = TreeNode(nums[mid])
        node.left = self.build(nums, low, mid - 1)
        node.right = self.build(nums, mid + 1, high)
        return node


solution = Solution()
nums = [0, 1, 2, 3, 4, 5]
tree = solution.sortedArrayToBST(nums)
print(tree)

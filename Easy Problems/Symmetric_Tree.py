'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
'''


from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirrored(root.left, root.right)

    def isMirrored(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if (p is None and q is None):
            return True

        if (p is None and q is not None) or \
                (q is None and p is not None):
            return False

        if p.val != q.val:
            return False

        return self.isMirrored(p.left, q.right) and self.isMirrored(p.right, q.left)


solution = Solution()
tree = TreeNode(1, TreeNode(3, None, None), TreeNode(3, None, None))
isSymmetric = solution.isSymmetric(tree)
print(f"The given tree is symmetric: {isSymmetric}")

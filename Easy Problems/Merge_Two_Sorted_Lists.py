'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        zerothNode = ListNode()
        current = zerothNode

        while (list1 is not None) or (list2 is not None):
            if list1 is not None and list2 is None:
                current.next = ListNode(list1.val, None)
                current = current.next
                list1 = list1.next
                continue

            if list1 is None and list2 is not None:
                current.next = ListNode(list2.val, None)
                current = current.next
                list2 = list2.next
                continue

            if list1.val <= list2.val:
                current.next = ListNode(list1.val, None)
                current = current.next
                list1 = list1.next
            else:
                current.next = ListNode(list2.val, None)
                current = current.next
                list2 = list2.next

        return zerothNode.next


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

solution = Solution()
merged = solution.mergeTwoLists(list1, list2)

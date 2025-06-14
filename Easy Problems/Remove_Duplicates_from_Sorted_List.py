'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
 
Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head: ListNode):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head

        while current is not None:
            next = current.next
            while next is not None:
                if next.val == current.val:
                    current.next = next.next
                next = next.next
            current = current.next
        return head


input = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
solution = Solution()
output = solution.deleteDuplicates(input)
print(output)

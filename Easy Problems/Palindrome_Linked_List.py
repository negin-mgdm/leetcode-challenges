'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
'''


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        strList = ""
        cur = first
        while cur:
            strList += str(cur.val)
            cur = cur.next
        return strList == strList[::-1]


solution = Solution()
first = ListNode(1)
second = ListNode(2)
third = ListNode(2)
fourth = ListNode(1)
first.next = second
second.next = third
third.next = fourth
isPalindrome = solution.isPalindrome(first)
print(isPalindrome)

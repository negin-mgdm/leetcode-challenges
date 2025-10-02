/*
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
*/

class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    isPalindrome(head) {
        let strList = "";
        let cur = head;
        while (cur) {
            strList += cur.val.toString();
            cur = cur.next;
        }
        return strList === strList.split("").reverse().join("");
    }
}

const solution = new Solution();
const first = new ListNode(1);
const second = new ListNode(2);
const third = new ListNode(2);
const fourth = new ListNode(1);

first.next = second;
second.next = third;
third.next = fourth;

const isPalindrome = solution.isPalindrome(first);
console.log(isPalindrome);
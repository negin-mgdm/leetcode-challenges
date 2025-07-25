/*
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
*/


// Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function (head) {
    let current = head;

    while (current !== null && current.next !== null) {
        if (current.val === current.next.val) {
            current.next = current.next.next;
        } else {
            current = current.next;
        }
    }

    return head;
};

// Helper function to print the linked list
function printList(head) {
    const result = [];
    while (head !== null) {
        result.push(head.val);
        head = head.next;
    }
    console.log(result);
}

// Input: [1,1,2,3,3]
const input = new ListNode(1,
    new ListNode(1,
        new ListNode(2,
            new ListNode(3,
                new ListNode(3)))));

const output = deleteDuplicates(input);
printList(output);
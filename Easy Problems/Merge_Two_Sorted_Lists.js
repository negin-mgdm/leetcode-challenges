/*
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
*/

//Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
    let zerothNode = new ListNode();
    let current = zerothNode;

    while (list1 !== null || list2 !== null) {
        if (list1 !== null && list2 === null) {
            current.next = new ListNode(list1.val);
            current = current.next;
            list1 = list1.next;
            continue;
        }

        if (list1 === null && list2 !== null) {
            current.next = new ListNode(list2.val);
            current = current.next;
            list2 = list2.next;
            continue;
        }

        if (list1.val <= list2.val) {
            current.next = new ListNode(list1.val);
            current = current.next;
            list1 = list1.next;
        } else {
            current.next = new ListNode(list2.val);
            current = current.next;
            list2 = list2.next;
        }
    }

    return zerothNode.next;
};

const list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
const list2 = new ListNode(1, new ListNode(3, new ListNode(4)));

let merged = mergeTwoLists(list1, list2);

function printList(head) {
    let current = head;
    let result = [];
    while (current !== null) {
        result.push(current.val);
        current = current.next;
    }
    console.log(result.join(" -> "));
}

printList(merged);
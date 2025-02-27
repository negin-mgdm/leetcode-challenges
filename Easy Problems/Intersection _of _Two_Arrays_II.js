/*
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
*/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
    let intersection = [];
    let nums1Map = new Map();

    for (let num of nums1) {
        if (nums1Map.has(num)) {
            nums1Map.set(num, nums1Map.get(num) + 1);
        } else {
            nums1Map.set(num, 1);
        }
    }

    for (let num of nums2) {
        if (nums1Map.has(num) && nums1Map.get(num) > 0) {
            intersection.push(num);
            nums1Map.set(num, nums1Map.get(num) - 1);
        }
    }

    return intersection;
};

let nums1 = [4, 9, 5];
let nums2 = [9, 4, 9, 8, 4];
console.log(intersect(nums1, nums2));
/*
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

Example 1:
Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

Example 2:
Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
 
Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
*/

/**
 * @param {string} s
 * @return {boolean}
 */
var areOccurrencesEqual = function (s) {
    let count = {};
    for (let char of s) {
        if (char in count) {
            count[char] += 1;
        } else {
            count[char] = 1;
        }
    }
    let valuesList = [];
    for (let value of Object.values(count)) {
        valuesList.push(value);
    }
    valuesList = new Set(valuesList);
    if (valuesList.size == 1) {
        return true;
    } else {
        return false;
    }
};

let s = "aaabb";
console.log(areOccurrencesEqual(s));
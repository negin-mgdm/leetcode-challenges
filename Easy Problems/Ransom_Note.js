/*
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
*/

/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
    let ransomCount = {};
    let magazineCount = {};

    for (let i of ransomNote) {
        if (ransomCount[i]) {
            ransomCount[i] += 1;
        } else {
            ransomCount[i] = 1;
        }
    }

    for (let i of magazine) {
        if (magazineCount[i]) {
            magazineCount[i] += 1;
        } else {
            magazineCount[i] = 1;
        }
    }

    for (let [char, count] of Object.entries(ransomCount)) {
        if (!magazineCount[char] || magazineCount[char] < count) {
            return false;
        }
    }

    return true;
};

let ransomNote = "aa";
let magazine = "aab";
console.log(canConstruct(ransomNote, magazine));